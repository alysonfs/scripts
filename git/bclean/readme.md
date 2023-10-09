# BClean
Script pensado para limpar branch's locais que não estão sendo mais usada. 

## Instalação

Vamos criar um executável, neste caso para MacOs.
> Quem puder fazer para os demais sistemas operacionais, agradeço.

Primeiro vamos instalar o pacote `PyInstaller` responsável por criar o executável.

```zsh
pip3 install pyinstaller
``` 

Agora vamos criar o executável.

```zsh
pyinstaller ./src/bclean.py 
```

Vamos agora alterar a permissão do arquivo para que possamos executar.

```zsh
chmod 755 ./dist/bclean/bclean
```

Precisamos agora mover o arquivo para uma pasta que esteja no PATH do sistema, para que possamos executar de qualquer lugar.

```zsh
mv ./dist/bclean/bclean /usr/local/bin
```
ou

Adicionar ao PATH do sistema a pasta onde o executável foi criado.

```zsh
export PATH=$PATH:/path/to/bclean
```


