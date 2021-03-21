import speedtest

print("SpeedTest")

print("******************************")

print("Contatos:")

print("Discord: _carlos#8479")

print("******************************")

def functions():
  
  print("Funçoes:")
  
  print("<1> Teste Velocidade Do Upload")
  
  print("<2> Teste Velocidade Do Download")
  
  print("<3> Teste Ping")

functions()

print("******************************")

st = speedtest.Speedtest()

useroption = int(input("Qual Opção Voce Escolhe: "))

if useroption == 1:
  
  SpeedTestUpload = st.upload()
  
  def printupload():
    
    print("Sua Taxa De Upload É: {}".format(SpeedTestUpload))
  
  printupload()

if useroption == 2:
  
  SpeedTestDownload = st.download()
  
  def printdownload():
    
    
    print("Sua Taxa De Download É: {}".format(SpeedTestDownload))
  
  printdownload()

if useroption == 3:
   
   ServerName = []
   
   st.get_servers(ServerName)
   
   SpeedTestPing = st.results.ping
   
   def printping():
     
     print("Seu Ping É: {}".format(SpeedTestPing))
    
   printping()
