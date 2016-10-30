#coding=utf-8
# import math
# import random
# import sys
# import time
import numpy as np
# import matplotlib.pyplot as plt
import os, re, sys
import xml.etree.ElementTree as etree  
import linecache

xsd=open(sys.argv[1],"r")
charge_file=sys.argv[2]


wcdzs={"Ac":"11","Ac_s":"9","Ag":"11","Al":"3","Al_h":"3","Ar":"8","As":"5","Au":"11","B":"3",
"B_h":"3","B_s":"3","Ba_sv":"10","Be":"2","Be_sv":"4","Bi":"5","Bi_d":"15","Br":"7",
"C":"4","C_h":"4","C_s":"4","Ca_pv":"8","Ca_sv":"10","Cd":"12","Ce":"12","Ce_3":"11",
"Cl":"7","Cl_h":"7","Co":"9","Cr":"6","Cr_pv":"12","Cs_sv":"9","Cu":"11","Cu_pv":"17",
"Dy_3":"9","Er_2":"8","Er_3":"9","Eu":"17","Eu_2":"8","F":"7","F_h":"7","F_s":"7",
"Fe":"8","Fe_pv":"14","Ga":"3","Ga_d":"13","Ga_h":"13","Gd":"18","Gd_3":"9","Ge":"4",
"Ge_d":"14","Ge_h":"14","H":"1","H.5":"0.5","H.75":"0.75","H_h":"1","H1.25":"1.25",
"H1.5":"1.5","He":"2","Hf":"4","Hf_pv":"10","Hg":"12","Ho_3":"9","I":"7","In":"3",
"In_d":"13","Ir":"9","K_pv":"7","K_sv":"9","Kr":"8","La":"11","La_s":"9","Li":"1",
"Li_sv":"3","Lu":"25","Lu_3":"9","Mg":"2","Mg_pv":"8","Mn":"7","Mn_pv":"13","Mo":"6",
"Mo_pv":"12","N":"5","N_h":"5","N_s":"5","Na":"1","Na_pv":"7","Na_sv":"9","Nb_pv":"11",
"Nb_sv":"13","Nd":"14","Nd_3":"11","Ne":"8","Ni_pv":"16","Np":"15","Np_s":"15","O":"6",
"O_h":"6","O_s":"6","Os":"8","Os_pv":"14","P":"5","P_h":"5","Pa":"13","Pa_s":"11",
"Pb":"4","Pb_d":"14","Pd":"10","Pd_pv":"16","Pm":"15","Pm_3":"11","Pr":"13","Pr_3":"11",
"Pt":"10","Pu":"16","Pu_s":"16","Rb_pv":"7","Rb_sv":"9","Re":"7","Re_pv":"13","Rh":"9",
"Rh_pv":"15","Ru":"8","Ru_pv":"14","S":"6","S_h":"6","Sb":"5","Sc_sv":"11","Se":"6",
"Si":"4","Si_h":"4","Sm":"16","Sm_3":"11","Sn":"4","Sn_d":"14","Sr_sv":"10","Ta":"5",
"Ta_pv":"11","Tb_3":"9","Tc":"7","Tc_pv":"13","Te":"6","Th":"12","Th_s":"10","Ti":"4",
"Ti_pv":"10","Ti_sv":"12","Tl":"3","Tl_d":"13","Tm":"23","Tm_3":"9","U":"14","U_s":"14",
"V":"5","V_pv":"11","V_sv":"13","W":"6","W_pv":"12","Xe":"8","Y_sv":"11","Yb":"24",
"Yb_2":"8","Zn":"12","Zr":"4","Zr_sv":"12"}

tree = etree.parse(xsd)
root = tree.getroot()
# print root.attrib
Atom3d_list=tree.findall("AtomisticTreeRoot/SymmetrySystem/MappingSet/MappingFamily/IdentityMapping/Atom3d")

ch_num=3
charge=[]
while linecache.getline(charge_file , ch_num):
	line=linecache.getline(charge_file , ch_num)
	if len(line)<80:
		charge.append(re.split(r"\s+",line.strip())[4])
	else :
		break
	ch_num+=1
# print charge


for i ,atom in enumerate(Atom3d_list):
	atom.attrib["Charge"]=str(float(charge[i])-float(wcdzs[atom.attrib["Components"]]))
	# print atom.attrib["ID"]
tree.write(sys.argv[1][:-4]+"_charge.xsd", encoding="utf-8",xml_declaration=True)