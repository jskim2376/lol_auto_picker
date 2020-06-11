import pyautogui
from urllib import request
import os
from PIL import Image
import re
import time
import pyperclip

class lolAutoPick():
    champion_list=[
        'Aatrox', 'Ahri', 'Akali', 'Alistar', 'Amumu', 'Anivia', 'Annie', 'Aphelios', 'Ashe', 'AurelionSol', 'Azir',
        'Bard', 'Blitzcrank', 'Brand', 'Braum',
        'Caitlyn', 'Camille', 'Cassiopeia', 'Chogath', 'Corki',
        'Darius', 'Diana', 'DrMundo', 'Draven',
        'Ekko', 'Elise', 'Evelynn', 'Ezreal',
        'Fiddlesticks', 'Fiora', 'Fizz', 
        'Galio', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 
        'Hecarim', 'Heimerdinger', 
        'Illaoi', 'Irelia', 'Ivern', 
        'Janna', 'JarvanIV', 'Jax', 'Jayce', 'Jhin', 'Jinx', 
        'Kaisa', 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kayn', 'Kennen', 'Khazix', 'Kindred', 'Kled', 'KogMaw', 
        'Leblanc', 'LeeSin', 'Leona', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 
        'Malphite', 'Malzahar', 'MonkeyKing', 'Maokai', 'MasterYi', 'MissFortune', 'Mordekaiser', 'Morgana', 
        'Nami', 'Nasus', 'Nautilus', 'Neeko', 'Nidalee', 'Nocturne', 'Nunu', 
        'Olaf', 'Orianna', 'Ornn', 
        'Pantheon', 'Poppy', 'Pyke', 
        'Qiyana', 'Quinn', 
        'Rakan', 'Rammus', 'RekSai', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 
        'Sejuani', 'Senna', 'Sett', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona', 'Soraka', 'Swain', 'Sylas', 'Syndra', 
        'TahmKench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'TwistedFate', 'Twitch', 
        'Udyr', 'Urgot', 
        'Varus', 'Vayne', 'Veigar', 'Velkoz', 'Vi', 'Viktor', 'Vladimir', 'Volibear', 
        'Warwick', 
        'Xayah', 'Xerath', 'XinZhao', 
        'Yasuo', 'Yorick', 'Yuumi', 
        'Zac', 'Zed', 'Ziggs', 'Zilean', 'Zoe', 'Zyra'
    ]
    def __init__(self):
        f = open('img/resolution.txt', 'r')
        self.currentResoulution = f.readline()
        f.close()

    def acceptGame(self):
        dn=pyautogui.locateCenterOnScreen('img/etc/'+self.currentResoulution+'/accept.png', confidence=0.9)
        if dn:
            pyautogui.click(dn)
            return True
        return False

    def firstChat(self, text):
        dn=pyautogui.locateCenterOnScreen('img/etc/'+self.currentResoulution+'/chat.png')
        print(dn)
        if dn:
            pyautogui.move()
            pyautogui.click(dn)
            before_copied = pyperclip.paste()
            pyperclip.copy(text)
            for i in range(10):
                pyautogui.hotkey('ctrl','v')
                pyautogui.press('enter')
            pyperclip.copy(before_copied)
            return True
        return False
<<<<<<< HEAD
        
=======
    def check_pick_champ_location(self):
        return pyautogui.locateCenterOnScreen('img/champion/randomeChampion.png',confidence=0.9)
>>>>>>> master
    def selectChampion(self, champ):
        if not champ:
            return False
        randChampLocate=pyautogui.locateCenterOnScreen('img/champion/'+self.currentResoulution+'/randomeChampion.png', confidence=0.9)
        print('champion location')
        print(randChampLocate)
        if randChampLocate:
            pyautogui.moveTo(randChampLocate)
            for i in range(1000):
                pyautogui.scroll(-500*i)
                champLocate=pyautogui.locateCenterOnScreen('img/champion/'+self.currentResoulution+'/'+champ+'.png',confidence=0.7)
                if champLocate:
                    pyautogui.click(champLocate)
                    pickLocate = pyautogui.locateCenterOnScreen('img/etc/'+self.currentResoulution+'/championPick.png', confidence=0.9)
                    pyautogui.click(pickLocate)
                    return True
            else:
                return False

    def selectSpell(self, spell1, spell2):
        if not spell1 or not spell2:
            return False
        spells=os.listdir('img/spell/'+self.currentResoulution)
    
        p=re.compile('choiced*')
        for spell in spells[:]:
            if not p.match(spell):
                spells.remove(spell)

        #find spell choice window location
        selectSpells=[]
        for spell in spells:
            selectSpell=pyautogui.locateCenterOnScreen('img/spell/'+self.currentResoulution+'/'+spell)
            if selectSpell: 
                selectSpells.append(selectSpell)

        #스펠을 선택하는 창의 위치를 못찾았을 경우 False
        if len(selectSpells) < 2:
            return False

        if selectSpells[0].x < selectSpells[1].x:
            pyautogui.click(selectSpells[0])
            spell1Locate = pyautogui.locateCenterOnScreen('img/spell/'+self.currentResoulution+'/'+spell1+'.png')
            pyautogui.click(spell1Locate)
            time.sleep(0.3)
            pyautogui.click(selectSpells[1])
            spell2Locate = pyautogui.locateCenterOnScreen('img/spell/'+self.currentResoulution+'/'+spell2+'.png')
            pyautogui.click(spell2Locate)
        else:
            pyautogui.click(selectSpells[1])
            spell1Locate = pyautogui.locateCenterOnScreen('img/spell/'+self.currentResoulution+'/'+spell1+'.png')
            pyautogui.click(spell1Locate)
            time.sleep(0.3)
            pyautogui.click(selectSpells[0])
            spell2Locate = pyautogui.locateCenterOnScreen('img/spell/'+self.currentResoulution+'/'+spell2+'.png')
            pyautogui.click(spell2Locate)

        print(selectSpells)
        return True
        
    def selectRune(self, mainRune, subRune, statRun):
        None

    def championImageDownload(self, champ):
        request.urlretrieve('https://ddragon.leagueoflegends.com/cdn/10.1.1/img/champion/'+champ+'.png', 'img/champion/1920/'+champ+'.png')
    
    def checkChampionDownload(self):
        dirlist = os.listdir('img/champion/1920')
        for champ in self.champion_list:
            if champ+'.png' not in dirlist:
                return False
        return True  

    def championCrop(self):
        champs = os.listdir("img/champion/")
        for champ in champs:
            champImage = Image.open('img/champion/'+champ)
            cropChamp = champImage.crop((10,10,110,110))
            cropChamp.save('img/champion/'+champ)

    def championResize(self):
        champs = os.listdir("img/champion/1920")
        
        for champ in champs:
            print(champ)
            champImage = Image.open('img/champion/1920/'+champ)
            rate = self.getResizeRate(1920, 1600)     
            resizeImage = champImage.resize((int(champImage.size[0]*rate),int(champImage.size[0]*rate)))
            resizeImage.save('img/champion/1600/'+champ)
        for champ in champs:
            print(champ)
            champImage = Image.open('img/champion/1920/'+champ)
            rate = self.getResizeRate(1920, 1280)     
            resizeImage = champImage.resize((int(champImage.size[0]*rate),int(champImage.size[0]*rate)))
            resizeImage.save('img/champion/1280/'+champ)
        for champ in champs:
            print(champ)
            champImage = Image.open('img/champion/1920/'+champ)
            rate = self.getResizeRate(1920, 1024)    
            resizeImage = champImage.resize((int(champImage.size[0]*rate),int(champImage.size[0]*rate)))
            resizeImage.save('img/champion/1024/'+champ)

    def getResizeRate(self, resoulution1, resolution2):
        return resolution2/resoulution1

if __name__ == "__main__":
    lap = lolAutoPick()
    lap.championResize() 