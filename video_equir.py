import os
import cv2 
import glob
import argparse
import lib.Equirec2Perspec as E2P

def equir2pers(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    
    for input_img in glob.glob(input_folder + '/*.jpg'): 
        equ = E2P.Equirectangular(input_img)  # Load equirectangular image

        for i in range(6): 
            theta = 60 * i
            img = equ.GetPerspective(90, theta, 0, 1280, 1280)  # FOV, theta, phi, height, width
            base_name = os.path.basename(input_img)
            output_path = os.path.join(output_folder, f'{base_name}_perspective_{i + 1}.png')
            cv2.imwrite(output_path, img)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('input_folder', help='input_folder')
    parser.add_argument('output_folder', help='output_folder')
    args = parser.parse_args()
    equir2pers(args.input_folder, args.output_folder)
