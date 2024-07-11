from glayout.flow.pdk.sky130_mapped import sky130_mapped_pdk as sky130
from glayout.flow.blocks.diff_pair import diff_pair
from glayout.flow.blocks.opamp import opamp
from glayout.flow.blocks.current_mirror import current_mirror
from tapeout.tapeout_and_RL.sky130_nist_tapeout import sky130_add_currmirror_labels

comp = current_mirror(sky130)
# comp = opamp(sky130)
# comp = diff_pair(sky130)
comp.name = 'currmirr'
comp.write_gds('out1.gds')
net = comp.info['netlist'].generate_netlist()
sky130.lvs_netgen(comp, comp.name, netlist=net, copy_intermediate_files=True)


# with open('ports2.txt', 'w') as f:
#     for port in comp.get_ports_list():
#         f.write(str(port) + '\n')
