from sky130_nist_tapeout import *
from glayout.flow.pdk.sky130_mapped import sky130_mapped_pdk as sky130
import os, sys
sys.path.append(os.path.join(os.path.abspath(__file__), "..", ".."))
from glayout.flow.blocks.diff_pair import diff_pair
from gdsfactory.component import Component
from subprocess import Popen, PIPE
from glayout.flow.blocks.current_mirror import current_mirror
import shutil 

import multiprocessing as mp
cpu_count = mp.cpu_count() 

if len(os.sched_getaffinity(0)) < cpu_count:
    try:
        os.sched_setaffinity(0, range(cpu_count))
    except OSError:
        print('Could not set affinity')
        
def custom_run( 
    comp_name: str,
    params, 
    index: int, 
    temperature_info: tuple[int,str]=(25,"normal model"),
    cload: float=0.0,
    noparasitics: bool=False,
    hardfail: bool=False, 
    tmpdirname: Optional[Union[str,Path]]=None,
    prepex: bool=False
):
    global pdk
    global PDK_ROOT
    # if not tmpdirname.is_dir():
    #     tmpdirname.mkdir(parents=True, exist_ok=True)
    # dest_gds_copy = save_gds_dir / (str(index)+".gds")
    sky130pdk = pdk 
    try: 
        if comp_name == "diffpair":
            new_params = diff_pair_parameters_de_serializer(params)
            component = sky130_add_diffpair_labels(diff_pair(sky130, **new_params))
        elif comp_name == "opamp":
            new_params = opamp_parameters_de_serializer(params)
            component = sky130_add_opamp_labels(sky130_add_lvt_layer(opamp(sky130, **new_params)))
        else:
            component = sky130_add_currmirror_labels(current_mirror(sky130, **params))
        component.name = comp_name
        area = float(component.area())
        
        # tmpdirname = Path(__file__).parent.resolve() / f"{comp_name}_run"
        tmp_gds_path = Path(tmpdirname / f"{comp_name}.gds").resolve()
        
        component.write_gds(str(tmp_gds_path))
        # if tmp_gds_path.is_file():
        #     dest_gds_copy.write_bytes(tmp_gds_path.read_bytes())
        
        extract_bash_template = str()
        with open("extract.bash.template", "r") as extraction_script:
            extract_bash_template = extraction_script.read()
            extract_bash_template = extract_bash_template.replace("@@PDK_ROOT", PDK_ROOT).replace("@@@PAROPT", "noparasitics" if noparasitics else "na").replace("@@@PREPEX", "yes" if prepex else "no")
        
        with open(str(tmpdirname)+"/extract.bash", "w") as extraction_script:
            extraction_script.write(extract_bash_template)
        
        copyfile(f"{comp_name}_perf_eval.sp", str(tmpdirname / f"{comp_name}_perf_eval.sp"))
        copytree("sky130A", str(tmpdirname / "sky130A"), dirs_exist_ok=True)
        
        Popen(["bash", "extract.bash", tmp_gds_path, component.name], cwd=tmpdirname).wait()
        print(f"Running simulation at temperature: {temperature_info[0]}C")
        
        process_spice_testbench(str(tmpdirname / f"{comp_name}_perf_eval.sp"), temperature_info=temperature_info)
        
        if comp_name == "opamp":
            process_netlist_subckt(str(tmpdirname / f"{comp_name}_pex.spice"), temperature_info[1], cload=cload, noparasitics=noparasitics)
        
        rename(str(tmpdirname / f"{comp_name}_pex.spice"), str(tmpdirname / f"{comp_name}_pex.spice"))
        
        Popen(["ngspice", "-b", f"{comp_name}_perf_eval.sp"], cwd=tmpdirname).wait()
        
        ac_file = tmpdirname / "result_ac.txt"
        ac_flag = 1 if ac_file.is_file() else 0
        power_file = tmpdirname / "result_power.txt"
        power_flag = 1 if power_file.is_file() else 0
        noise_file = tmpdirname / "result_noise.txt"
        noise_flag = 1 if noise_file.is_file() else 0
        
        result_dict = get_sim_results(ac_file, power_file, noise_file)
        result_dict["area"] = area
        
        if comp_name == "diffpair":
            results = diff_pair_results_serializer(**result_dict)
        elif comp_name == "opamp":
            results = opamp_results_serializer(**result_dict)
        else:
            results = currmirror_results_serializer(**result_dict)
        print(f'\n\n******* RESULTS ********: {results}\n\n')
        
        with open('output.txt', 'w') as f:
            f.write(f"Results for {comp_name} run {index} with the following params: \n{params}")
            f.write(f"\n\n******* RESULTS ********: \n{results}\n\n")
    
        shutil.rmtree(str(tmpdirname) + "sky130A")
        # delete the above extra files with shutil
        delete_files = [".ext", ".nodes", ".res.ext", ".sim"]
        for file in delete_files:
            if os.path.exists(str(tmpdirname) + f"/*{file}"):
                os.remove(str(tmpdirname) + f"/*{file}")
                
        # if output_dir is not None:
        #     if isinstance(output_dir, int):
        #         output_dir = save_gds_dir / f"dir_{output_dir}"
        #         output_dir = Path(output_dir).resolve()
        #     else:
        #         output_dir = Path(output_dir).resolve()
            
        #     output_dir.mkdir(parents=True, exist_ok=True)
            
        #     if not output_dir.is_dir():
        #         raise ValueError("Output directory must be a directory")
            
        #     copytree(str(tmpdirname), str(output_dir / "test_output"), dirs_exist_ok=True)
        
    except Exception as e_LorA:
        if hardfail:
            raise e_LorA
        if comp_name == "diffpair":
            results = diff_pair_results_serializer()
        elif comp_name == "opamp":
            results = opamp_results_serializer()
        else:
            results = currmirror_results_serializer()
        with open('get_training_data_ERRORS.log', 'a') as errlog:
            errlog.write(f"\n{comp_name} run {index} with the following params failed: \n{params}")
        

def extract_only(comp_name, params, tmpdirname: Path, noparasitics: bool=False, prepex: bool=False):
    if not tmpdirname.is_dir():
        tmpdirname.mkdir(parents=True, exist_ok=True)
    # currmirror_v = sky130_add_currmirror_labels(current_mirror(sky130, numcols = numcols))
    # currmirror_v.name = f"currmirror_{numcols}"
    if comp_name == "diffpair":
        component = sky130_add_diffpair_labels(diff_pair(sky130, **params))
    elif comp_name == "opamp":
        component = sky130_add_opamp_labels(sky130_add_lvt_layer(opamp(sky130, **params)))
    else:
        component = sky130_add_currmirror_labels(current_mirror(sky130, **params))
    component.name = comp_name
    area = float(component.area())
    tmp_gds_path = Path(f"./{comp_name}_run/{comp_name}.gds").resolve()
    component.write_gds(tmp_gds_path)
    with open("extract.bash.template","r") as extraction_script:
        extractbash_template = extraction_script.read()
        extractbash_template = extractbash_template.replace("@@PDK_ROOT",PDK_ROOT).replace("@@@PAROPT","noparasitics" if noparasitics else "na").replace("@@@PREPEX", "yes" if prepex else "no")
    with open(str(tmpdirname)+"/extract.bash","w") as extraction_script:
        extraction_script.write(extractbash_template)
    #copyfile("extract.bash",str(tmpdirname)+"/extract.bash")
    copyfile(f"{comp_name}_perf_eval.sp",str(tmpdirname)+f"/{comp_name}_perf_eval.sp")
    copytree("sky130A",str(tmpdirname)+"/sky130A", dirs_exist_ok=True)
    # extract layout
    Popen(["bash","extract.bash", tmp_gds_path, component.name],cwd=tmpdirname).wait()
    
    shutil.rmtree(str(tmpdirname) + "/sky130A")
    # delete the above extra files with shutil
    delete_files = [".ext", ".nodes", ".res.ext", ".sim"]
    for file in delete_files:
        if os.path.exists(str(tmpdirname) + f"/*{file}"):
            os.remove(str(tmpdirname) + f"/*{file}")



if __name__ == "__main__":
    
    # extract_only(heredir)
    # parse arguments 
    parser = argparse.ArgumentParser()
    parser.add_argument("--component", type=str, help="component to run", required=True, choices=["diffpair","opamp","currmirror"])
    
    if sys.argv[-1] == "diffpair":
        heredir = Path(__file__).parent.resolve() / "diffpair_run" / "nets"
        params = get_diffpair_params_list(test_mode=False)
        # params = diff_pair_parameters_de_serializer(diff_pair_parameters_serializer())
        comp_name = "diffpair"
        index = 0
        
        
    elif sys.argv[-1] == "currmirror":
        
        heredir = Path(__file__).parent.resolve() / "currmirror_run" / "nets"
        params = currmirror_parameters_de_serializer(currmirror_parameters_serializer())
        comp_name = "currmirror"
        index = 0

        # extract_only(tmpdirname=heredir, noparasitics=False)
        
    elif sys.argv[-1] == "opamp":
        heredir = Path(__file__).parent.resolve() / "opamp_run" / "nets"
        params = get_small_parameter_list(test_mode=False)
        # params = opamp_parameters_de_serializer(opamp_parameters_serializer())
        print(params)
        comp_name = "opamp"
        index = 0
    
    n = max(len(os.sched_getaffinity(0)), 128)
    print('Using', n, 'processes for the pool')
    dir1 = heredir / "postpex"
    dir2 = heredir / "prepex"
    # dir1.mkdir(parents=True, exist_ok=True)
    # dir2.mkdir(parents=True, exist_ok=True)
    
    with Pool(n) as cores:
        # cores.starmap(extract_only, [(comp_name, params, heredir / f'run_{i}', False, True) for i in range(25)])
        cores.starmap(custom_run, [(comp_name, params[i], i, (25, "normal_mode"), 0.0, False, False, Path(dir1 / f"run_{i}"), False) for i in range(len(params))])
        cores.starmap(custom_run, [(comp_name, params[i], i, (25, "normal_mode"), 0.0, False, False, Path(dir2 / f"run_{i}"), True) for i in range(len(params))])
        
        
    # custom_run(comp, comp_name, index)
    # params = diff_pair_parameters_serializer()
    # __run_single_brtfrc(0, params, save_gds_dir=Path(__file__).parent.resolve() / "diffpair_run")