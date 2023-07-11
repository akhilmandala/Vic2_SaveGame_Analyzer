from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from SandPfinder import generate_states_and_provinces

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-s", "--save-file", help="Target save file")
parser.add_argument("-sf", "--save-folder", help="Target saves folder")
parser.add_argument("-m", "--mod-folder", help="Mod folder")
parser.add_argument("-o", "--output-folder", help="Output folder")
args = vars(parser.parse_args())

save_file = args["save-file"]
mod_directory = args["mod-folder"]
output_directory = args["output-directory"]

generate_states_and_provinces(mod_directory)

if(save_file):
    #single file analysis

    pass;
else:
    #batch process
    pass;