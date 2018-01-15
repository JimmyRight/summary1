# -*- coding: utf-8 -*-
import wx;
import wx.media;
import os;
import SPrint;
import mediaStateBar;
import mediaList;
import SaveLog;
import MediaItem;
woldcart = "media files|*.*|avi|*.avi|rmvb|*.rmvb|rm|*.rm|wma|*.wma|mp3|*.mp3";
class MediaFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,wx.NewId(),u"媒体播放器",pos=wx.DefaultPosition,size=(500,500));
        self.media = '';
        try:
            self.media = wx.media.MediaCtrl(self,style=wx.SIMPLE_BORDER,
                                             #szBackend=wx.media.MEDIABACKEND_DIRECTSHOW
                                             #szBackend=wx.media.MEDIABACKEND_QUICKTIME
                                             #szBackend=wx.media.MEDIABACKEND_WMP10
                                             );
            self.media.Bind(wx.media.EVT_MEDIA_LOADED,self.mediaLoaded);
            self.media.Bind(wx.media.EVT_MEDIA_STATECHANGED,self.mediaStateChange)
        except NotImplementedError:
            self.Destroy()
            raise;
        self.listView = '';
        self.item = MediaItem.MediaItem();
        self.sb = mediaStateBar.MediaStateBar(self);
        self.SetStatusBar(self.sb);
        self.log = SaveLog.SaveLog();
        #self.log.test();
        self.menu = wx.Menu()
        self.openMenu = self.menu.Append(wx.NewId(),u"打开文件");
        self.Bind(wx.EVT_MENU,self._openFile,self.openMenu);
        self.quitMenu = self.menu.Append(wx.NewId(),u"退出");
        self.Bind(wx.EVT_MENU,self.quit,self.quitMenu);
        self.viewMenu = wx.Menu();
        self.listMenu = self.viewMenu.Append(wx.NewId(),u"打开播放列表");
        self.Bind(wx.EVT_MENU,self.openList,self.listMenu);
        self.loadListMenu = self.viewMenu.Append(wx.NewId(),u"加载播放列表");
        self.Bind(wx.EVT_MENU,self.loadMediaList,self.loadListMenu);
        self.saveListMenu = self.viewMenu.Append(wx.NewId(),u"保存播放列表")
        self.Bind(wx.EVT_MENU,self.saveMediaList,self.saveListMenu);
        menuBar = wx.MenuBar();
        menuBar.Append(self.menu,u"文件")
        menuBar.Append(self.viewMenu,u"播放列表")
        self.SetMenuBar(menuBar);
        self.slider = wx.Slider(self,wx.NewId(), 0,0,100);
        self.Bind(wx.EVT_SLIDER,self.onSeek,self.slider);
        self.btnGroupSizer = wx.BoxSizer(wx.HORIZONTAL);
        self.btnGroupSizer.Add((5,5),0)
        self.playBtn = self.createButton("./pic/play.png",self.playMp3,u"播放");
        self.playBtn.Disable()
        self.btnGroupSizer.Add(self.playBtn);
        self.btnGroupSizer.Add((5,5),0)
        self.pauseBtn = self.createButton("./pic/pause.png",self.pauseMp3,u"暂停");
        self.pauseBtn.Disable()
        self.btnGroupSizer.Add(self.pauseBtn);
        self.btnGroupSizer.Add((5,5),0)
        self.stopBtn = self.createButton("./pic/stop.png",self.stopMp3,u"停止");
        self.stopBtn.Disable()
        self.btnGroupSizer.Add(self.stopBtn);
        self.btnGroupSizer.Add((5,5),0)
        self.preBtn = self.createButton("./pic/pre.png",self.preMp3,u"前一个");
        self.preBtn.Disable()
        self.btnGroupSizer.Add(self.preBtn);
        self.btnGroupSizer.Add((5,5),0)
        self.nextBtn = self.createButton("./pic/next.png",self.nextMp3,u"下一个");
        self.nextBtn.Disable()
        self.btnGroupSizer.Add(self.nextBtn);
        self.btnGroupSizer.Add((5,5),0)
        self.openBtn = self.createButton("./pic/media.png",self._openFile,u"打开文件");
        #self.openBtn.Disable()
        self.btnGroupSizer.Add(self.openBtn);
        self.btnGroupSizer.Add((5,5),0)
        self.listBtn = self.createButton("./pic/list.png",self.openList,u"打开列表");
        #self.listBtn.Disable()
        self.btnGroupSizer.Add(self.listBtn)
        self.btnGroupSizer.Add((5,5),0)
        self.volSlider = wx.Slider(self,wx.NewId(), 0,0,100);
        self.Bind(wx.EVT_SLIDER,self.volumeSeek,self.volSlider);
        self.btnGroupSizer.Add(self.volSlider)
        self.btnGroupSizer.Add((5,5),0)
        self.volTxt = wx.StaticText(self,wx.NewId(),"")
        self.btnGroupSizer.Add(self.volTxt)
        self.btnGroupSizer.Add((5,5),0)
        mainSizer = wx.BoxSizer(wx.VERTICAL);
        mainSizer.Add(self.media,1,wx.EXPAND|wx.ALL,5);
        #mainSizer.Add((5,5),0)
        mainSizer.Add(self.slider,0,wx.EXPAND|wx.ALL,5);
        #mainSizer.Add((2,2),0)
        mainSizer.Add(self.btnGroupSizer,0,wx.EXPAND|wx.ALL,5);
        #mainSizer.Add((2,2),0)
        self.SetSizer(mainSizer);
        self.Layout();
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER,self.onTimer);
        self.timer.Start(200);
    def createButton(self,img,clickFun,tip=""):
        bmp = wx.Bitmap(img, wx.BITMAP_TYPE_PNG);
        btn = wx.BitmapButton(self,wx.NewId(),bmp);
        if tip != '' : btn.SetToolTipString(tip);
        btn.Bind(wx.EVT_BUTTON,clickFun);
        return btn;
    def quit(self,event):
        self.Destroy();
    def playMp3(self,e):
        if self.item != '':
            self.media.Play()
       # self.media.SetInitialSize()
    def pauseMp3(self,e=''):
        self.media.Pause()
    def stopMp3(self,e=''):
        self.media.Stop()
    def preMp3(self,e):
        if self.item!='':
            self.item = self.log.getPreItem(self.item.index)
            if self.item != '':
                self.playMedia(self.item.url,self.item.fileName);
    def nextMp3(self,e):
        if self.item!='':
            self.item = self.log.getNextItem(self.item.index)
            if self.item != '':
                self.playMedia(self.item.url,self.item.fileName);
    def onSeek(self,event):
        self.media.Seek(self.slider.GetValue())
    def callAfterPlayMedia(self,url):
        #self.media.SetInitialSize();
        self.media.Play();
    def playMedia(self,url,filename):
        #print SPrint.encodeFromSystem( u"播放文件: " ) , SPrint.encodeFromSystem(url) ;
        if self.media.Load(url) != True:
            return ;
        self.item = MediaItem.MediaItem();
        self.item.fileName = filename;
        self.item.url = url;
        self.SetTitle(filename)
        self.SetStatusText(filename,1)
        #wx.FutureCall(2000,self.callAfterPlayMedia,url);
    def _openFile(self,event):
        dialog = wx.FileDialog(self,u"打开文件",'F://movie//',"",woldcart,style=wx.OPEN|wx.CHANGE_DIR)
        if dialog.ShowModal() == wx.ID_OK:
            self.playMedia(dialog.GetPath(),dialog.GetFilename())
        dialog.Destroy();
    def cellRemove(self,url,all=False):
        if all == True:
            self.stopMp3()
            self.item = '';
            return ;
        if self.item.url == url:
            self.stopMp3();
            self.item = '';
    def volumeSeek(self,evt):
        #print float(self.volSlider.GetValue()/100);
        self.media.SetVolume(self.volSlider.GetValue()/100.0)
        self.volTxt.SetLabel(str(self.volSlider.GetValue())+'%')
    def mediaLoaded(self,e):
        print "media loaded!"
        self.media.Play();
        self.slider.SetRange(0,self.media.Length());
        self.item.length = self.getAccurateTime(self.media.Length()/1000);
        if self.log.addItem(self.item):
            if self.listView != '':
                self.listView.reflash(self.log);
        if self.log.haveNextItem(self.item.index):
            self.nextBtn.Enable();
        else:
            self.nextBtn.Disable()
        if self.log.havePreItem(self.item.index):
            self.preBtn.Enable()
        else:
            self.preBtn.Disable();
        self.volSlider.SetValue(self.media.GetVolume()*100);
        self.volTxt.SetLabel(str(self.volSlider.GetValue())+'%')
    def mediaStateChange(self,evt):
        if self.media.GetState() == wx.media.MEDIASTATE_PAUSED:
            self.playBtn.Enable()
            self.pauseBtn.Disable()
            self.stopBtn.Enable();
            self.SetStatusText(u"暂停")
        elif self.media.GetState() == wx.media.MEDIASTATE_PLAYING:
            self.playBtn.Disable()
            self.pauseBtn.Enable()
            self.stopBtn.Enable();
            self.SetStatusText(u"播放")
        elif self.media.GetState() == wx.media.MEDIASTATE_STOPPED:
            self.playBtn.Enable()
            self.pauseBtn.Enable()
            self.stopBtn.Disable();
            self.SetStatusText(u"停止")
    def onTimer(self,evt):
        self.slider.SetValue(self.media.Tell());
        self.SetStatusText(self.creatTimeStatusTEXT(),1)
    def creatTimeStatusTEXT(self):
        current = self.getAccurateTime(self.media.Tell()/1000);
        total = self.getAccurateTime(self.media.Length()/1000);
        return '  ' + current + '/' + total;
    def openList(self,evt):
        if self.listView == '':
            self.listView = mediaList.MediaListView(self,self.log);
            self.listView.CenterOnParent(wx.BOTH);
            self.listView.Show();
            self.listView.Bind(wx.EVT_CLOSE,self.closeOpenList);
        else:
            self.closeOpenList(evt);
    def closeOpenList(self,evt):
        self.listView.Destroy();
        self.listView = '';
    def loadMediaList(self,evt):
        woldcart1 = "txt|*.txt";
        dialog = wx.FileDialog(self,u"加载播放列表",'C:',"",woldcart1,style=wx.OPEN|wx.CHANGE_DIR)
        if dialog.ShowModal() == wx.ID_OK:
            self._loadMediaList(dialog.GetPath())
        dialog.Destroy();
    def _loadMediaList(self,url):
        f = file(url)
        lines = f.readlines()
        for line in lines:
            if line:
                self.log.loadLog(line);
    def saveMediaList(self,evt):
        woldcart1 = "txt|*.txt";
        dialog = wx.FileDialog(self,u"保存播放列表",'C:',"",woldcart1,style=wx.SAVE|wx.CHANGE_DIR)
        if dialog.ShowModal() == wx.ID_OK:
            self._saveMediaList(dialog.GetPath())
        dialog.Destroy();
    def _saveMediaList(self,url):
        f = file(url,"w+")
        f.writelines(self.log.createLog());
        f.close();
        self.showMessage(u"保存成功！");
    def showMessage(self,str):
        dlg = wx.MessageDialog(self, str,u"消息", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
    def getAccurateTime(self,s):
      h = 0
      m = 0
      if s/60 !=0:
          m = s/60
          s = s%60
      if m/60 !=0:
          h = m/60
          m = m%60
      return str(h)+':'+str(m)+':'+str(s)

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MediaFrame();
    bmp = wx.Icon("./pic/media.png",wx.BITMAP_TYPE_PNG)
    frame.SetIcon(bmp)
    frame.Show();
    app.MainLoop();