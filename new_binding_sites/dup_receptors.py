########################################################################################
#
#  Author: Sally R. Ellingson
#  Date: Aug. 8, 2013
#  Usage: python dup_receptors.py $receptors $sites $new
#  $receptors = path to directory containing receptor pdbqt files
#  $sites = path to directory containing pdb files for all the docking sites
#  $new = path to directory where receptor pdbqt files will be saved named after each site
#
##########################################################################################

import sys, glob, os

if len(sys.argv) < 4:
  print "Usage: python dup_receptors.py $receptors $sites $new\n$receptors = path to directory containing receptor pdbqt files\n$sites = path to directory containing pdb files for all the docking sites\n$new = path to directory where receptor pdbqt files will be saved named after each site"
  sys.exit(0)

pdbqt_dir=sys.argv[1]
site_list=glob.glob(sys.argv[2]+'/*.pdb')
new_dir=sys.argv[3]

for site in site_list:
  sitesplit=site.split('/')
  newbase=sitesplit[len(sitesplit)-1][:-4]
  oldbase=newbase.split('site')[0][:-1]
  os.system('cp '+pdbqt_dir+'/'+oldbase+'.pdbqt '+new_dir+'/'+newbase+'.pdbqt')

