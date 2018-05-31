# -*- coding: utf-8 -*-
from GALANK07 import *
from datetime import datetime
import json, time, random, tempfile, os, sys, pytz
import codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse, ast
from gtts import gTTS
from googletrans import Translator
from urllib.parse import urlencode
from io import BytesIO, UnsupportedOperation

#Galank = LineClient(id='EMAILMU', passwd='PASSWORDMU')
Galank = LineClient(authToken='TOKENMU SAYANG') 
Galank.log("Auth Token : " + str(Galank.authToken))
#========================================================
channel = LineChannel(Galank)
Galank.log("Channel Access Token : " + str(channel.channelAccessToken))
#========================================================
GalankProfile = Galank.getProfile()
GalankSettings = Galank.getSettings()
GalankPoll = LinePoll(Galank)
GalankMID = Galank.profile.mid
#call = LineCall(Galank)

contact = Galank.getProfile()
backup = Galank.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
#====================================

helpMessage ="""╭════════╬╬════════╮
        ʜᴇʟᴘ menu
╰════════╬╬════════╯
╭════════╬╬════════╮
╠⎆ Me
╠⎆ Mymid
╠⎆ Myname
╠⎆ Mybio
╠⎆ Mypicture
╠⎆ Myvideoprofile
╠⎆ Mycover
╠⎆ Stealprofile「@」
╠⎆ Unsend me
╠⎆ Getsq
╠⎆ Lc 「@」
╠⎆ Gc 「@」
╠⎆ Sticker: 「angka」
╠⎆ Yt: 「text」
╠⎆ Image: 「text」
╠⎆ Gcreator
╠⎆ Say: 「text」
╠⎆ Apakah 「text」
╠⎆ Sytr: 「text」
╠⎆ Tr: 「text」
╠⎆ Speed
╠⎆ Pict 「@」
╠⎆ Cover 「@」
╠⎆ Tagall
╠⎆ Ceksider
╠⎆ Offread
╠⎆ Listgroup
╠⎆ Restart
╠⎆ Friendlist
╠⎆ Cloneprofile 「@」
╠⎆ Restoreprofile
╠⎆ Lurking 「on/off」
╠⎆ Lurking
╠⎆ Invgroupcall
╠⎆ Lurking reset
╠⎆ kick 「@」
╠⎆ Self on
╠⎆ Public on
╠⎆ Public
╰════════╬╬════════╯
╭════════╬╬════════╮
╠⎆ CRΣΔTΩR βΨ:
╠⎆ 『✍͡➴͜Ĝα₤αηĸ͜͡✫』
╠⎆ sᴜᴘᴘᴏʀᴛᴇᴅ ʙʏ  : 
╠⎆ TΣΔM SLΔCҜβΩT
╰════════╬╬════════╯
line.me/ti/p/~fuck.you__
"""
proMessage ="""
═══════════════●
║●╠[COMMAND SETTING]
║●╠═══════════════●
║●╠[Add] 
║●╠[Join] 
║●╠[Leave] 
║●╠[Read] 
║●╠[Inviteprotect] 
║●╠[Reread] 
║●╠[Qr] 
║●╠[Qrjoin] 
║●╠[Ck]
║●╠[Groupprotect]
║●╠[Kc]
║●╠[Ptt]
║●╠[Tag]
"""
poll = LinePoll(Galank)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
admin=['u78643d09e42a36836a17cc918963a8b7',GalankMID]
mode='self'
cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = clientProfile.displayName
myProfile["statusMessage"] = clientProfile.statusMessage
myProfile["pictureStatus"] = clientProfile.pictureStatus
#==========================================
#========================================
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
    
def music(songname):
    params = {'songname':songname}
    url = 'http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params)
    r = requests.get(url,verify=False).text
    data = json.loads(r)
    for song in data:
        return song[4]

def find(songname):
    params = {'songname':songname}
    url = 'http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params)
    r = requests.get(url,verify=False).text
    data = json.loads(r)
    for song in data:
        return song[4]

def findLyric(to,song):
    params = {'songname':song}
    r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?'+urllib.urlencode(params))
    data = r.text
    data = data.encode('utf-8')
    data = json.loads(data)
    for song in data:
        Galank.sendText(to,"Lyrics Of " + song[0] + ":\n\n"+ song[5])
    
#=======================================
while True:
    try:
        ops=poll.singleTrace(count=50)
        if ops != None:
          for op in ops:
#=========================================================================================================================================#
            #if op.type in OpType._VALUES_TO_NAMES:
            #    print("[ {} ] {}".format(str(op.type), str(OpType._VALUES_TO_NAMES[op.type])))
#=========================================================================================================================================#
            if op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                to = receiver
                sender = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            Galank.sendChatChecked(receiver, msg_id)
                            contact = Galank.getContact(sender)            
                            if text.lower() == 'me':
                                Galank.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                            elif text.lower() == 'mymid':
                                Galank.sendMessage(msg.to,"[MID]\n" +  GalankMID)
                            elif text.lower() == 'myname':
                                me = Galank.getContact(clientMID)
                                Galank.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                            elif text.lower() == 'mybio':
                                me = Galank.getContact(GalankMID)
                                Galank.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                            elif text.lower() == 'mypicture':
                                me = Galank.getContact(GalankMID)
                                Galank.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                            elif text.lower() == 'myvideoprofile':
                                me = Galank.getContact(GalankMID)
                                Galank.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                            elif text.lower() == 'mycover':
                                me = Galank.getContact(clientMID)
                                cover = channel.getProfileCoverURL(GalankMID)    
                                Galank.sendImageWithURL(msg.to, cover)
                            elif "stealprofile" in msg.text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = Galank.getContact(ls)
                                        cu = channel.getProfileCoverURL(ls)
                                        path = str(cu)
                                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                        Galank.sendMessage(msg.to,"Nama :\n" + contact.displayName + "\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage)
                                        Galank.sendImageWithURL(msg.to,image)
                                        Galank.sendImageWithURL(msg.to,path)
                            elif "cloneprofile" in msg.text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    for mention in mentionees:
                                        contact = mention["M"]
                                        break
                                    try:
                                        Galank.cloneContactProfile(contact)
                                        Galank.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                                    except:
                                        client.sendMessage(msg.to, "Gagal clone member")
                            elif text.lower() == 'restoreprofile':
                                try:
                                    GalankProfile.displayName = str(myProfile["displayName"])
                                    GalankProfile.statusMessage = str(myProfile["statusMessage"])
                                    GalankProfile.pictureStatus = str(myProfile["pictureStatus"])
                                    Galank.updateProfileAttribute(8, GalankProfile.pictureStatus)
                                    Galank.updateProfile(GalankProfile)
                                    Galank.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                                except:
                                    Galank.sendMessage(msg.to, "Gagal restore profile")
#====================================================
                            elif text.lower() == 'announce':
                                gett = Galank.getChatRoomAnnouncements(receiver)
                                for a in gett:
                                    aa = Galank.getContact(a.creatorMid).displayName
                                    bb = a.contents
                                    cc = bb.link
                                    textt = bb.text
                                    Galank.sendText(receiver, 'Link: ' + str(cc) + '\nText: ' + str(textt) + '\nMaker: ' + str(aa))
#----------------Commandtambahan----------------------#
                            elif msg.text in ["Listgroup"]:
                               gid = Galank.getGroupIdsJoined()
                               h = ""
                               for i in gid:
                                h += "「⏣」 %s  \n" % (client.getGroup(i).name + " | 「Members 」: " + str(len (client.getGroup(i).members)))
                               Galank.sendText(msg.to, "⊙「Group List」⊙\n"+ h +"⊙「Total Group」 : " +str(len(gid)))
#===================================================
                            elif text.lower() == 'unsend me':
                                Galank.unsendMessage(msg_id)
                            elif text.lower() == 'getsq':
                                a = Galank.getJoinedSquares()
                                squares = a.squares
                                members = a.members
                                authorities = a.authorities
                                statuses = a.statuses
                                noteStatuses = a.noteStatuses
                                txt = str(squares)+'\n\n'+str(members)+'\n\n'+str(authorities)+'\n\n'+str(statuses)+'\n\n'+str(noteStatuses)+'\n\n'
                                txt2 = ''
                                for i in range(len(squares)):
                                    txt2 += str(i+1)+'. '+str(squares[i].invitationURL)+'\n'
                                Galank.sendText(receiver, txt2)
                            elif 'lc ' in text.lower():
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = Galank.getContact(u).mid
                                    s = Galank.getContact(u).displayName
                                    hasil = channel.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        channel.like(str(sender), str(result), likeType=random.choice(typel))
                                        channel.comment(str(sender), str(result), 'Auto Like by ●TΣΔM SLΔCҜβΩT●\n line.me/ti/p/~fuck.you__')
                                    Galank.sendText(receiver, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                                except Exception as e:
                                    Galank.sendText(receiver, str(e))
                            elif 'gc ' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    cname = Galank.getContact(u).displayName
                                    cmid = Galank.getContact(u).mid
                                    cstatus = Galank.getContact(u).statusMessage
                                    cpic = Galank.getContact(u).picturePath
                                    Galank.sendText(receiver, 'Nama : '+cname+'\nMID : '+cmid+'\nStatus Msg : '+cstatus+'\nPicture : http://dl.profile.line.naver.jp'+cpic)
                                    Galank.sendMessage(receiver, None, contentMetadata={'mid': cmid}, contentType=13)
                                    if Galank.getContact(u).videoProfile != None:
                                        Galank.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                                    else:
                                        Galank.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic)
                                except Exception as e:
                                    Galank.sendText(receiver, str(e))
                            elif 'sticker:' in msg.text.lower():
                                try:
                                    query = msg.text.replace("sticker:", "")
                                    query = int(query)
                                    if type(query) == int:
                                        Galank.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        Galank.sendText(receiver, 'https://line.me/S/sticker/'+str(query))
                                    else:
                                        Galank.sendText(receiver, 'gunakan key sticker angka bukan huruf')
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif "yt:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("yt:", "")
                                    query = query.replace(" ", "+")
                                    x = Galank.youtube(query)
                                    Galank.sendText(receiver, x)
                                except Exception as e:
                                    Galank.sendText(receiver, str(e))
                            elif "image:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("image:", "")
                                    images = Galank.image_search(query)
                                    Galank.sendImageWithURL(receiver, images)
                                except Exception as e:
                                    Galank.sendText(receiver, str(e))
                            elif 'say:' in msg.text.lower():
                                try:
                                    isi = msg.text.lower().replace('say:','')
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp.mp3')
                                    Galank.sendAudio(receiver, 'temp.mp3')
                                except Exception as e:
                                    Galank.sendText(receiver, str(e))
                            elif 'apakah ' in msg.text.lower():
                                try:
                                    txt = ['iya','tidak','bisa jadi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    Galank.sendAudio(receiver, 'temp2.mp3')
                                except Exception as e:
                                    Galank.sendText(receiver, str(e))
                            elif "sytr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text
                                    tts = gTTS(text=A, lang=isi[1], slow=False)
                                    tts.save('temp3.mp3')
                                    Galank.sendAudio(receiver, 'temp3.mp3')
                                except Exception as e:
                                    Galank.sendText(receiver, str(e))
#============================================================#HELPSTART#=========================================================#
                            elif text.lower() == 'key':
                                Galank.sendText(msg.to,helpMessage)
                                print ("[COMMAND] HELP")
                            elif text.lower() == 'pro':
                                Galank.sendText(msg.to,proMessage)
                                print ("[COMMAND] HELP")
                                
                            elif text.startswith("imagetext "):
                                sep = text.split(" ")
                                textnya = text.replace(sep[0] + " ","")   
                                urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                                Galank.sendImageWithURL(msg.to, urlnya)   
                                
                            elif text.startswith("musik "):
                                try:
                                    sep = msg.text.split(" ")
                                    songname = msg.text.replace(sep[0] + " ","")
                                    params = {'songname': songname}
                                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.parse.urlencode(params))
                                    data = r.text
                                    data = json.loads(data)
                                    for song in data:
                                        hasil = 'This is Your Music\n'
                                        hasil += 'Judul : ' + song[0]
                                        hasil += '\nDurasi : ' + song[1]
                                        hasil += '\nLink Download : ' + song[4]
                                        Galank.sendMessage(msg.to, hasil)
                                        Galank.sendMessage(msg.to, "Please Wait for Music...")
                                        Galank.sendAudioWithURL(msg.to, song[4])
                                except Exception as njer:
                                        Galank.sendMessage(msg.to, str(njer))      
					
                        #Galank.sendMessage(msg.to, str(e))
 #               elif text.lower() == 'add on':
 #                   settings["autoAdd"] = True
#                    Galank.sendMessage(to, "Auto Add ✔")
 #               elif text.lower() == 'add off':
#                    settings["autoAdd"] = False
#                    Galank.sendMessage(to, "Auto Add ✘")
#                elif text.lower() == 'join on':
#                    settings["autoJoin"] = True
 #                   Galank.sendMessage(to, "Join ✔")
#                elif text.lower() == 'join off':
 #                   settings["autoJoin"] = False
#                    Galank.sendMessage(to, "Join ✘")
 #               elif text.lower() == 'leave on':
 #                   settings["autoLeave"] = True
 #                   Galank.sendMessage(to, "Leave ✔")
#                elif text.lower() == 'leave off':
 #                   settings["autoLeave"] = False
 #                   Galank.sendMessage(to, "Leave ✘")
 #               elif text.lower() == 'contact on':
#                    settings["contact"] = True
 #                   Galank.sendMessage(to, "Contact ✔")
 #               elif text.lower() == 'contact off':
 #                   settings["contact"] = False
#                    Galank.sendMessage(to, "Contact ✘")
#============================================================#MODE / RESTART#======================================================#
                            elif text.lower() == 'restart':
                                Galank.sendText(receiver, '「Bot restart」')
                                print ("BOT RESTART")
                                restart_program()
                            elif text.lower() == 'friendlist':
                                contactlist = Galank.getAllContactIds()
                                kontak = Galank.getContacts(contactlist)
                                num=1
                                msgs="═════════List Friend═════════"
                                for ids in kontak:
                                    msgs+="\n[%i] %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                                Galank.sendMessage(msg.to, msgs)
#============================================================#ULTI STARTR#=========================================================#
                            elif 'kick' in text.lower():
                                   targets = []
                                   key = eval(msg.contentMetadata["MENTION"])
                                   key["MENTIONEES"] [0] ["M"]
                                   for x in key["MENTIONEES"]:
                                       targets.append(x["M"])
                                   for target in targets:
                                       try:
                                           Galank.kickoutFromGroup(msg.to,[target])                           
                                       except:
                                           Galank.sendText(msg.to,"Error")
#======================================================             
                            elif text == "invgroupcall":
                                if msg.toType == 2:
                                    group = Galank.getGroup(to)
                                    members = [mem.mid for mem in group.members]
                                    call.acquireGroupCallRoute(to)
                                    call.inviteIntoGroupCall(to, contactIds=members)
                                    Galank.sendMessage(to, "Done invite group call")                                         
#===============================================================================================================#
                            elif msg.text in ["Gcreator"]:
                              if msg.toType == 2:
                                    ginfo = Galank.getGroup(msg.to)
                                    gCreator = ginfo.creator.mid
                                    try:
                                        gCreator1 = ginfo.creator.displayName

                                    except:
                                        gCreator = "Error"
                                    Galank.sendMessage(receiver, None, contentMetadata={'mid': gCreator}, contentType=13)
                                    Galank.sendText(msg.to, "「Group Creator」 : " + gCreator1)
                                    Galank.tag(receiver, gCreator)
#===================
                            elif "tr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text                               
                                    Galank.sendText(receiver, str(A))
                                except Exception as e:
                                    Galank.sendText(receiver, str(e))
                            elif text.lower() == 'speed':
                                start = time.time()
                                Galank.sendText(receiver, "██████████████99%Complete...")
                                elapsed_time = time.time() - start
                                Galank.sendText(receiver, "%sdetik" % (elapsed_time))
                            elif 'pict' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = Galank.getContact(u).pictureStatus
                                    if Galank.getContact(u).videoProfile != None:
                                        Galank.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a+'/vp.small')
                                    else:
                                        Galank.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                                except Exception as e:
                                    Galank.sendText(receiver, str(e))
                            elif 'cover' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    Galank.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    Galank.sendText(receiver, str(e))
                            elif text.lower() == 'tagall':
                                group = Galank.getGroup(receiver)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 100:
                                    client.mention(receiver, nama)
                                if jml > 100 and jml < 200:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, len(nama)):
                                        nm2 += [nama[j]]
                                    Galank.mention(receiver, nm2)
                                if jml > 200 and jml < 300:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    Galank.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    Galank.mention(receiver, nm3)
                                if jml > 300 and jml < 400:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    Galank.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    Galank.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    Galank.mention(receiver, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    Galank.mention(receiver, nm4)
                                if jml > 400 and jml < 501:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    Galank.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    Galank.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    Galank.mention(receiver, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    Galank.mention(receiver, nm4)
                                    for m in range(401, len(nama)):
                                        nm5 += [nama[m]]
                                    Galank.mention(receiver, nm5)             
                                Galank.sendText(receiver, "Members :"+str(jml))
                            elif text.lower() == 'ceksider':
                                try:
                                    del cctv['point'][receiver]
                                    del cctv['sidermem'][receiver]
                                    del cctv['cyduk'][receiver]
                                except:
                                    pass
                                cctv['point'][receiver] = msg.id
                                cctv['sidermem'][receiver] = ""
                                cctv['cyduk'][receiver]=True
                            elif text.lower() == 'offread':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][receiver]=False
                                    Galank.sendText(receiver, cctv['sidermem'][msg.to])
                                else:
                                    Galank.sendText(receiver, "Heh belom di Set")
                            elif text.lower() == 'self on':
                                mode = 'self'
                                Galank.sendText(receiver, 'Mode Public Off')
                            elif text.lower() == 'public on':
                                mode = 'public'
                                Galank.sendText(receiver, 'Mode Public ON')
                            elif text.lower() == 'restart':
                                restart_program()
                      #                LOOK SIDER                  #                    
                            elif text.lower() == 'lurking on':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read['readPoint']:
                                        try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                            del read['readTime'][msg.to]
                                        except:
                                            pass
                                        read['readPoint'][msg.to] = msg.id
                                        read['readMember'][msg.to] = ""
                                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                        read['ROM'][msg.to] = {}
                                        with open('sider.json', 'w') as fp:
                                            json.dump(read, fp, sort_keys=True, indent=4)
                                            Galank.sendMessage(msg.to,"Lurking already on")
                                else:
                                    try:
                                        del read['readPoint'][msg.to]
                                        del read['readMember'][msg.to]
                                        del read['readTime'][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][msg.to] = msg.id
                                    read['readMember'][msg.to] = ""
                                    read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                    read['ROM'][msg.to] = {}
                                    with open('sider.json', 'w') as fp:
                                        json.dump(read, fp, sort_keys=True, indent=4)
                                        Galank.sendMessage(msg.to, "Set reading point:\n" + readTime)
                                        
                            elif text.lower() == 'lurking off':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to not in read['readPoint']:
                                    Galank.sendMessage(msg.to,"Lurking already off")
                                else:
                                    try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                            del read['readTime'][msg.to]
                                    except:
                                          pass
                                    Galank.sendMessage(msg.to, "Delete reading point:\n" + readTime)
                
                            elif text.lower() == 'lurking reset':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read["readPoint"]:
                                    try:
                                        read["readPoint"][msg.to] = True
                                        read["readMember"][msg.to] = {}
                                        read["readTime"][msg.to] = readTime
                                        read["ROM"][msg.to] = {}
                                    except:
                                        pass
                                    Galank.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                                else:
                                    Galank.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                                    
                            elif text.lower() == 'lurking':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        Galank.sendMessage(receiver,"[ Reader ]:\nNone")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = client.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = 'Lurkers:\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\nLurking time: \n" + readTime
                                    try:
                                        Galank.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    Galank.sendMessage(receiver,"Lurking has not been set.")
                except Exception as e:
                    Galank.log("[SEND_MESSAGE] ERROR : " + str(e))
#=========================================================================================================================================#
                elif text.lower() == 'groupprotect on':
                    settings["protect"] = True
                    Galank.sendMessage(to, "Protect ✔")
                elif text.lower() == 'groupprotect off':
                    settings["protect"] = False
                    Galank.sendMessage(to, "Protect ✖")
                elif text.lower() == 'inviteprotect on':
                    settings["inviteprotect"] = True
                    Galank.sendMessage(to, "Invit Pro ✔")
                elif text.lower() == 'inviteprotect off':
                    settings["inviteprotect"] = False
                    Galank.sendMessage(to, "Invit Pro ✖")
                elif text.lower() == 'qr on':
                    settings["qrprotect"] = True
                    Galank.sendMessage(to, "Qr ✔")
                elif text.lower() == 'qr off':
                    settings["qrprotect"] = False
                    Galank.sendMessage(to, " Qr ✖")
                elif text.lower() == 'reread on':
                    settings["reread"] = True
                    Galank.sendMessage(to, "ReRead ✔")
                elif text.lower() == 'reread off':
                    settings["reread"] = False
                    Galank.sendMessage(to, "ReRead ✖")
                elif text.lower() == 'read on':
                    settings["autoRead"] = True
                    Galank.sendMessage(to, "Read ✔")
                elif text.lower() == 'read off':
                    settings["autoRead"] = False
                    Galank.sendMessage(to, "Read ✖")
                elif text.lower() == 'qrjoin on':
                    settings["autoJoinTicket"] = True
                    Galank.sendMessage(to, "Qr Join  ✔")
                elif text.lower() == 'qrjoin off':
                    settings["autoJoinTicket"] = False
                    Galank.sendMessage(to, "Qr join ✖")
                elif text.lower() == 'tag on':
                    settings["detectMention"] = False
                    Galank.sendMessage(to, "Tag ✔")
                elif text.lower() == 'tag off':
                    settings["detectMention"] = True
                    Galank.sendMessage(to, "Tag ✖")
                elif text.lower() == 'ck on':
                    settings["checkSticker"] = True
                    Galank.sendMessage(to, "Stickers ✔")
                elif text.lower() == 'ck off':
                    settings["checkSticker"] = False
                    Galank.sendMessage(to, "Stickers ✖")
                elif text.lower() == 'kc on':
                    settings["kickContact"] = True
                    Galank.sendMessage(to, "Kick Contact ✔")
                elif text.lower() == 'kc off':
                    settings["kickContact"] = False
                    Galank.sendMessage(to, "Kick Contact ✖")
                elif text.lower() == 'ptt on':
                    settings["autoPtt"] = True
                    Galank.sendMessage(to, "Ptt ✔")
                elif text.lower() == 'ptt off':
                    settings["autoPtt"] = False
                    Galank.sendMessage(to, "ptt ✖")

            elif mode == 'public ' and op.type == 26:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            Galank.sendChatChecked(receiver, msg_id)
                            contact = Galank.getContact(sender)
                            if text.lower() == 'me':
                                Galank.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                                Galank.tag(receiver, sender)
                            elif 'gc ' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    cname = Galank.getContact(u).displayName
                                    cmid = Galank.getContact(u).mid
                                    cstatus = Galank.getContact(u).statusMessage
                                    cpic = Galank.getContact(u).picturePath
                                    Galank.sendText(receiver, 'Nama : '+cname+'\nMID : '+cmid+'\nStatus Msg : '+cstatus+'\nPicture : http://dl.profile.line.naver.jp'+cpic)
                                    Galank.sendMessage(receiver, None, contentMetadata={'mid': cmid}, contentType=13)
                                    if Galank.getContact(u).videoProfile != None:
                                        Galank.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                                    else:
                                        Galank.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic)
                                except Exception as e:
                                    Galank.sendText(receiver, str(e))                            
                            elif 'sticker:' in msg.text.lower():
                                try:
                                    query = msg.text.replace("sticker:", "")
                                    query = int(query)
                                    if type(query) == int:
                                        Galank.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        Galank.sendText(receiver, 'https://line.me/S/sticker/'+str(query))
                                    else:
                                        Galank.sendText(receiver, 'gunakan key sticker angka bukan huruf')
                                except Exception as e:
                                    Galank.sendText(receiver, str(e))
                            elif "yt:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("yt:", "")
                                    query = query.replace(" ", "+")
                                    x = Galank.youtube(query)
                                    Galank.sendText(receiver, x)
                                except Exception as e:
                                    Galank.sendText(receiver, str(e))
                            elif "image:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("image:", "")
                                    images = Galank.image_search(query)
                                    Galank.sendImageWithURL(receiver, images)
                                except Exception as e:
                                    Galank.sendText(receiver, str(e))
                            elif 'say:' in msg.text.lower():
                                try:
                                    isi = msg.text.lower().replace('say:','')
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp.mp3')
                                    Galank.sendAudio(receiver, 'temp.mp3')
                                except Exception as e:
                                    Galank.sendText(receiver, str(e))
                            elif 'apakah ' in msg.text.lower():
                                try:
                                    txt = ['iya','tidak','bisa jadi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    Galank.sendAudio(receiver, 'temp2.mp3')
                                except Exception as e:
                                    Galank.sendText(receiver, str(e))
                            elif "sytr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text
                                    tts = gTTS(text=A, lang=isi[1], slow=False)
                                    tts.save('temp3.mp3')
                                    Galank.sendAudio(receiver, 'temp3.mp3')
                                except Exception as e:
                                    Galank.sendText(receiver, str(e))
                            elif "tr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text                               
                                    Galank.sendText(receiver, str(A))
                                except Exception as e:
                                    Galank.sendText(receiver, str(e))
                            elif text.lower() == 'speed':
                                start = time.time()
                                Galank.sendText(receiver, "██████████████99%Complete...")
                                elapsed_time = time.time() - start
                                Galank.sendText(receiver, "%sdetik" % (elapsed_time))
                            elif 'pict' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = Galank.getContact(u).pictureStatus
                                    if Galank.getContact(u).videoProfile != None:
                                        Galank.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a+'/vp.small')
                                    else:
                                        Galank.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                                except Exception as e:
                                    Galank.sendText(receiver, str(e))
                            elif 'cover' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    Galank.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    Galank.sendText(receiver, str(e))
                except Exception as e:
                    Galank.log("[SEND_MESSAGE] ERROR : " + str(e))
#=========================================================================================================================================#
#(op):
    #try:
        if op.type == 0:
            return
        if op.type == 5:
            contact = Galank.getContact(op.param1)
            print ("[ 5 ] Notice Add Contact : " + contact.displayName)
            if settings["autoAdd"] == True:
                Galank.findAndAddContactsByMid(op.param1)
                Galank.sendMessage(op.param1, "Terimakasih Telah Invite 👌😳".format(str(contact.displayName)))
                Galank.sendMessage(op.param1, "Jangan Nakalin dedek,  Achu Masih polos kakak 😳^^")
        if op.type == 11:
            group = Galank.getGroup(op.param1)
            contact = Galank.getContact(op.param2)
            if settings["qrprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    gs = Galank.getGroup(op.param1)
                    gs.preventJoinByTicket = True
                    araragi.updateGroup(gs)
                    invsend = 0
                    Galank.sendMessage(op.param1,Galank.getContact(op.param2).displayName + "Heh kutil babik jangan buka qr ！")
                    Galank.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 13:
            contact1 = Galank.getContact(op.param2)
            contact2 = Galank.getContact(op.param3)
            group = Galank.getGroup(op.param1)
            if settings["inviteprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    Galank.cancelGroupInvitation(op.param1,[op.param3])
                    time.sleep(0.15)
                    Galank.kickoutFromGroup(op.param1,[op.param3])
                    time.sleep(0.15)
                    Galank.kickoutFromGroup(op.param1,[op.param2])
            if GalankMID in op.param3:
                if settings["autoJoin"] == True:
                    try:
                        arrData = ""
                        text = "%s "%('[on]')
                        arr = []
                        mention = "@x "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention + "\nAssalamualaikum.. "
                        Galank.acceptGroupInvitation(op.param1)
                        Galank.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        Galank.sendMessage(op.param1, "Created ：")
                        Galank.sendContact(op.param1, "u78643d09e42a36836a17cc918963a8b7")
                    except Exception as error:
                        print(error)
            if GalankMID in op.param3:
                if settings["autoPtt"] == True:
                    Galank.acceptGroupInvitation(op.param1)
                    Galank.sendMessage(op.param1, "SeeYou...")
                    Galank.leaveGroup(op.param1)
        if op.type == 15:
            contact1 = Galank.getContact(op.param2)
            group = Galank.getGroup(op.param1)
            if settings["seeLeave"] == True:
                try:
                    arrData = ""
                    text = "%s "%('[Hallo.. ]')
                    arr = []
                    mention = "@x "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "Good Bye Kakak Semoga Amal ibadah mu cukup 😳{} ！".format(str(group.name))
                    Galank.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 17:
            contact1 = Galank.getContact(op.param2)
            group = Galank.getGroup(op.param1)
            if settings["seeJoin"] == True:
                try:
                    arrData = ""
                    text = "%s "%('Halo')
                    arr = []
                    mention = "@x "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "Cek note ya kakak Baca Rules nya！".format(str(group.name))
                    Galank.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 19:
            contact1 = Galank.getContact(op.param2)
            group = Galank.getGroup(op.param1)
            contact2 = Galank.getContact(op.param3)
            print ("[19] Notice Kick Out From Group: " + str(group.name) + "\n" + op.param1 +"\nNama: " + contact1.displayName + "\nMid:" + contact1.mid + "\nNama: " + contact2.displayName + "\nMid:" + contact2.mid )
            if settings["protect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    if settings["kickContact"] == True:
                        Galank.kickoutFromGroup(op.param1,[op.param2])
                        settings["blacklist"][op.param2] = True
                        time.sleep(0.1)
                        Galank.sendMessage(op.param1, "[Dangger] %s Kick %s"%(contact1.displayName,contact2.displayName))
                        Galank.sendMessage(op.param1, "Kick：")
                        sendMessageWithMention(op.param1, contact1.mid)
                        Galank.sendMessage(op.param1, " Kicker：")
                        sendMessageWithMention(op.param1, contact2.mid)
                    else:
                        Galank.kickoutFromGroup(op.param1,[op.param2])
                        settings["blacklist"][op.param2] = True
                        time.sleep(0.1)
            else:
                if settings["kickContact"] == True:
                    Galank.sendMessage(op.param1, "[Dangger] %s  Kick%s"%(contact1.displayName,contact2.displayName))
                    Galank.sendMessage(op.param1, " kick：")
                    sendMessageWithMention(op.param1, contact1.mid)
                    Galank.sendMessage(op.param1, "Kicker：")
                    sendMessageWithMention(op.param1, contact2.mid)
                else:
                    pass
        if op.type == 22:
            print ("[ 22 ] Notice Leave Group")
            if settings["autoLeave"] == True:
                Galank.leaveRoom(op.param1)
        if op.type == 1:
            print ("[1] NOTICED File Konfigurasi ")
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != Galank.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 7:
               if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    path = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ = "[ Info ]"
                    ret_ += "\nID       : {}".format(stk_id)
                    ret_ += "\nID       : {}".format(pkg_id)
                    ret_ += "\nUrl     : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\nPicUrl：https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ += "\n[ By : 『✍͡➴͜Ĝα₤αηĸ͜͡✫』: TΣΔM SLΔCҜβΩT ]"
                    Galank.sendMessage(to, str(ret_))
                    Galank.sendImageWithURL(to, path)
        if op.type == 26:
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.toType == 0:
                        Galank.log("[%s]"%(msg._from)+msg.text)
                    else:
                        Galank.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 65:
            try:
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            Galank.sendMessage(at,"[Pelaku Unsend ]\n%s\n[Unsend Messages ]\n%s"%(araragi.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                            print ["Ingat Pesan"]
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != araragi.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    Galank.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if msg.contentType == 0 and sender not in GalankMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if GalankMID in mention["M"]:
                                if settings["detectMention"] == False:
                                    contact = Galank.getContact(sender)
                                    Galank.sendMessage(to, "Jadi Orang Jangan Genit Napa? Ohh..Gwa Tau Pasti Mau Ngajak Mojok! Pc aja kak biar mesra 😘 😳 ") 
                                pass

            if op.type == 55:
                print ("[ 55 ] NOTIFIED READ MESSAGE")
                try:
                    if op.param1 in read['readPoint']:
                        if op.param2 in read['readMember'][op.param1]:
                            pass
                        else:
                            read['readMember'][op.param1] += op.param2
                        read['ROM'][op.param1][op.param2] = op.param2
                    else:
                       pass
                except:
                    pass         

            elif op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = client.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                pref=['eh ada','hai kak','aloo..','nah','lg ngapain','halo','sini kak']
                                Galank.sendText(op.param1, str(random.choice(pref))+' '+Name)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

            else:
                pass
#=========================================================================================================================================#
            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)
            
    except Exception as e:
        Galank.log("[SINGLE_TRACE] ERROR : " + str(e))
