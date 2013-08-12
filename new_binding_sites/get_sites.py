###################################################################
#
#  Author: Sally R. Elingson
#  Created: Aug. 7, 2013
#  Usage: python get_sites.py directory
#  where directory is the path to a directory containing .pdb files
#  containing docking sites named $receptorbasename_site$n.pdb
#
####################################################################

vmd = '/Users/sally/Applications/VMD\ 1.9.1.app/Contents/MacOS/startup.command'

import os, glob, sys, subprocess

if (len(sys.argv) != 2):
  print "Usage: python get_sites.py directory\nwhere directory is the path to a directory containing .pdb files\ncontaining docking sites named $receptorbasename_site$n.pdb\n"
  sys.exit(0)

#get name of directory containing site files and get file names
site_dir = sys.argv[1]
site_list = glob.glob(site_dir+'/*.pdb')

f1=open('receptors.txt', 'w')
f1.write('receptor size_x size_y size_z center_x center_y center_z\n')
f1.close()

#for each file
for site in site_list:
  #get the receptor basename for the site
  split_site=site.split('/')
  rec_base=split_site[len(split_site) - 1][:-4]
  os.system(vmd+' -dispdev text -eofexit < /Users/sally/work/docking_scripts/new_binding_sites/get_cell_dim.tcl -args ' + site + ' '+ rec_base)
