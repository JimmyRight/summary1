# -*- coding: utf-8 -*-
import wx;
import sys;
import os;
import SaveLog;
import subprocess;
class MediaListView(wx.MiniFrame):
    def __init__(self,parent,log):
        wx.MiniFrame.__init__(self,parent,wx.NewId(),u"文件列表",style=wx.DEFAULT_FRAME_STYLE);
        self.SetAutoLayout(True)
        self.mediaMain = parent;
        self.menu = '';
        self.selectIndex = -1
        self.listDataLog = SaveLog.SaveLog();
        self.listDataLog = log;
        self.listct = wx.ListCtrl(self,wx.NewId(),style=wx.LC_REPORT|
                                                          wx.LC_VRULES|
                                                          wx.LC_SORT_ASCENDING);
        self.listct.InsertColumn(0,u"编号")
        self.listct.SetColumnWidth(0,38)
        self.listct.InsertColumn(1,u"名字")
        self.listct.SetColumnWidth(1,235)
        self.listct.InsertColumn(2,u"时间");
        self.listct.SetColumnWidth(2,105)
        frSizer = wx.BoxSizer(wx.VERTICAL)
        frSizer.Add(self.listct,1,wx.EXPAND|wx.ALL,5)
        self.listct.Bind(wx.EVT_CONTEXT_MENU,self.onRightClick)
        self.listct.Bind(wx.EVT_LEFT_DCLICK,self.doubleClick)
        self.listct.Bind(wx.EVT_LIST_ITEM_SELECTED,self.itemSelected)
        self.SetSizer(frSizer)
        self.Layout();
        wx.CallAfter(self.reflash,self.listDataLog)
    def reflash(self,log=''):
        self.listct.DeleteAllItems();
        if log != '':
            self.listDataLog = log;
        i = 0;
        ls = log.getList();
        for it in ls:
            if it:
                index = self.listct.InsertStringItem(i,str(it.index));
                self.listct.SetStringItem(index,0,str(it.index))
                self.listct.SetStringItem(index,1,it.fileName)
                self.listct.SetStringItem(index,2,it.length)
                i = i+1;
    def onRightClick(self,evt):
        self.menu = wx.Menu();
        self.playMenu = self.menu.Append(wx.NewId(),u"播放")
        self.Bind(wx.EVT_MENU,self.cellPlay,self.playMenu)
        self.delMenu = self.menu.Append(wx.NewId(),u"删除")
        self.Bind(wx.EVT_MENU,self.cellRomve,self.delMenu);
        self.dirMenu = self.menu.Append(wx.NewId(),u"打开文件目录")
        self.Bind(wx.EVT_MENU,self.openDir,self.dirMenu);
        self.delAllMenu = self.menu.Append(wx.NewId(),u"清除播放列表")
        self.Bind(wx.EVT_MENU,self.clearAll,self.delAllMenu);
        self.PopupMenu(self.menu);
        self.menu.Destroy();
    def cellPlay(self,evt):
        self.selectIndex = self.listct.GetFirstSelected();
        item = self.listDataLog.getItemByIndex(self.selectIndex);
        self.mediaMain.playMedia(item.url,item.fileName);
    def cellRomve(self,evt):
        #self.selectIndex = self.listct.GetFirstSelected();
        url = self.listDataLog.delItemByIndex(self.listct.GetFirstSelected());
        self.listDataLog.reflashDataByIndex();
        self.reflash(self.listDataLog);
        self.mediaMain.cellRemove(url)
    def doubleClick(self,evt):
        item = self.listDataLog.getItemByIndex(self.selectIndex);
        self.mediaMain.playMedia(item.url,item.fileName);
        evt.Skip();
    def itemSelected(self,evt):
        self.selectIndex = evt.GetIndex();
        evt.Skip();
    def openDir(self,evt):
        self.selectIndex = self.listct.GetFirstSelected();
        item = self.listDataLog.getItemByIndex(self.selectIndex);
        subprocess.Popen("explorer " + os.path.split(item.url)[0]);
    def clearAll(self,evt):
        self.listDataLog.clearAll();
        self.reflash(self.listDataLog);
        self.mediaMain.cellRemove('',True)
