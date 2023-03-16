import os
import uuid
from PIL import Image
import wget

#python .\stylegan2\generate.py --outdir=out --trunc=0.7 --seeds=600 --network=.\stylegan2_models\StyleGAN2_microscopev1.pkl    <---- Zdjęcia pod mikroskopem
#python .\stylegan2\generate.py --outdir=out --trunc=0.7 --seeds=600 --network=.\stylegan2_models\Long_Krrrl_Drawings__final.pkl    <---- Rysunki
#python .\stylegan2\generate.py --outdir=out --trunc=0.7 --seeds=600 --network=.\stylegan2_models\mapdreamer.pkl   <---- Mapy
#python .\stylegan2\generate.py --outdir=out --trunc=0.7 --seeds=123 --network=.\stylegan2_models\network-snapshot-027750.pkl   <---- Ptaki
#python .\stylegan2\generate.py --outdir=out --trunc=0.7 --seeds=123 --network=.\stylegan2_models\stylegan2-horse-config-f.pkl   <---- Konie
#python .\stylegan2\generate.py --outdir=out --trunc=0.7 --seeds=123 --network=.\stylegan_models\stylegan2-ffhq-512x512  <---- Twarze
#python .\stylegan2\generate.py --outdir=out --trunc=0.7 --seeds=123 --network=.\stylegan2_models\stylegan2-church-config-f.pkl   <---- Kościoły
#python .\stylegan2\generate.py --outdir=out --trunc=0.7 --seeds=123 --network=.\stylegan2_models\stylegan2-car-config-f.pkl   <---- Samochody
#python .\stylegan2\generate.py --outdir=out --trunc=0.7 --seeds=123 --network=.\stylegan2_models\stylegan2-afhqcat-512x512.pkl   <---- Koty
#python .\stylegan2\generate.py --outdir=out --trunc=0.7 --seeds=123 --network=.\stylegan2_models\stylegan2-afhqdog-512x512.pkl  <---- Psy
#python .\stylegan2\generate.py --outdir=out --trunc=0.7 --seeds=123 --network=.\stylegan2_models\stylegan2-afhqwild-512x512.pkl  <---- Zwierzęta



class Generation:
    def __init__(self, target_model, target_seed, target_trunc):
        self.model = None
        if target_model == "CAT":
            self.model = 'stylegan2-afhqcat-512x512.pkl'

        if target_model == "DOG":
            self.model = 'stylegan2-afhqdog-512x512.pkl'

        if target_model == "QV2":
            self.model = 'stylegan2-ffhq-512x512.pkl'

        if target_model == "WILD":
            self.model = 'stylegan2-afhqwild-512x512.pkl'

        if target_model == "BRECAHAD":
            self.model = 'stylegan2-brecahad-512x512.pkl'

        if target_model == "CELEBAHQ":
            self.model = 'stylegan2-celebahq-256x256.pkl'

        if target_model == "METAFACES":
            self.model = 'stylegan2-metfaces-1024x1024.pkl'

        self.target_seed = target_seed
        self.target_trunc = target_trunc
        
    def get_model_name(self):
        return self.model


    def generate(self):
        #random directory name
        random_dir_name = str(uuid.uuid4())
        if self.target_seed == -1:
            #Generate random seed
            self.target_seed = str(uuid.uuid4().int)[:6]
        os.system(f'python /content/lesson/stylegan2/generate.py --outdir=/content/lesson/out/{random_dir_name} --trunc={self.target_trunc} --seeds={self.target_seed} --network=/content/lesson/stylegan2_models/{self.model}')
        #Wait for image to be generated
        while not os.path.exists(f'/content/lesson/out/{random_dir_name}'):
            pass
        for image_name in os.listdir(f'/content/lesson/out/{random_dir_name}'):
            #Open as PIL image
            image = Image.open(f'/content/lesson/out/{random_dir_name}/{image_name}')
            return image
        
    def download_model(self):
        return [f'https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan2/versions/1/files/{self.name}', f'/content/lesson/stylegan2_models/{self.name}']

        #https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan2/versions/1/files/stylegan2-afhqcat-512x512.pkl
        #https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan2/versions/1/files/stylegan2_afhqcat_512x512.pkl
        #https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan2/versions/1/files/stylegan2-afhqcat-512x512.pkl