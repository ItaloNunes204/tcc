import MTCNN
import Image
from os import listdir
from os.path import isdir
import asarray
 
detector = MTCNN()
 
def extrair_face(arquivo, size=(160,160) ):
   
    img = Image.open(arquivo)# caminho completo path
   
    img = img.convert('rgb')# converter em RGB
   
    array = asarray(img)
 
    results = detector.detect_faces(array)
 
    x1,y1,width,height = results[0]['box']
 
    x2 = x1 + width
 
    y2 = y1 + height
 
    face = array[y1:y2 , x1:x2]
 
    image = Image.fromarray(face)
    image = image.resize(size)
 
    return image
 
def flip_image(image):
    img = image.transpose(Image.FILP_LEFT_RIGHT)
    return img
 
 
def load_fotos(diretory_src, diretory_target):
    for filename in listdir(diretory_src):
 
        path = diretory_src + filename
        path_tg = diretory_target + "flip" + filename
 
        path_tg_flip= diretory_target + filename
        try:
            face = extrair_face(path)
            flip =flip_image(face)
 
            face.save(path_tg,'JPEG', quality = 100, optimize = True, progressive = True)
            face.save(path_tg_flip,'JPEG', quality = 100, optimize = True, progressive = True)
        except:
            print("erro na imagem {}".format(path))
 
def load_dir(diretory_src, diretory_target):
 
    for subdir in listdir(diretory_src):
 
        path = diretory_src + subdir + "\\"
 
        path_tg = diretory_target + subdir + "\\"
 
        if not isdir(path):
            continue
 
        load_fotos(path, path_tg)
 
if __name__ == '__main__' :
    load_dir( # aqui colocamos o caminho das fotos. lembra que tem que colocar mais uma barra
                "D:\\Arquivos Usuario\\Documents\\TCC\\FOTOS\\", "D:\\Arquivos Usuario\\Documents\\TCC\\FACES\\"
              # aqui colocamos o caminho das faces. lembra que tem que colocar mais uma barra
            )
