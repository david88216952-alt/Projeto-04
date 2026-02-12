# importação a biblioteca qrcode e PIL
import qrcode
from PIL import Image

# variavel que armazena o conteudo do QR Code


# criando a instancia do QRCode
def gerarQrCode (data, fileName):
  qr = qrcode.QRCode (
    version=1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
   )
   # adiciona o conteudo ao objeto QR Code
  qr.add_data(data)
  qr.make(fit=True)

  # cria a imagem do QR Code
  img = qr.make_image(fill_color="black" , back_color= "white")

  # salva a imagem em um arquivo
  img.save(fileName)
  print(f"QR Code gerado e salvo como '{fileName}'")

# interação com o usuario para obter o conteudo do QR Code

if __name__ == "__main__":
  user_data = input("Digite o conteudo para o QR Code (URL, texto, etc.): ")
  user_fileName = input("Digite o nome do arquivo para salvar o QR Code (qrcode.png): ")

print("QR Code gerado e salvo como 'qrcode.png'")



