import MediaItem;
class SaveLog():
    list = [];
    def addItem(self,it=MediaItem.MediaItem):
        if self.getItemByURL(it.url) == '' :
            it.index = len(self.list) + 1;
            self.list.append(it);
            return True;
        return False;
    def clearAll(self):
        self.list = [];
    def getItemByURL(self,url):
        for it in self.list:
            if it and it.url == url:
                return it;
        return '';
    def getItemByIndex(self,ind):
        return self.list[ind];
    def delItemByIndex(self,ind):
        it = self.getItemByIndex(ind);
        if it :
            url = it.url;
            self.list.remove(it);
            return url;
        return '';
    def reflashDataByIndex(self):
        i = 1;
        for it in self.list:
            if it:
                it.index = i;
                i = i+ 1;
    def havePreItem(self,ind):
        if ind-1>0:
            return True;
        return False;
    def haveNextItem(self,ind):
        if ind < len(self.list)-1:
            return True;
        return False;
    def getPreItem(self,ind):
        if ind>0:
            ind = ind -1;
            return self.list[ind];
        return '';
    def getNextItem(self,ind):
        if ind < len(self.list)-1:
            ind = ind + 1;
            return self.list[ind];
        return '';
    def getList(self):
        return self.list;
    def createLog(self):
        out = [];
        for it in self.list:
            if it:
                out.append(it.createLog())
        return out;
    def loadLog(self,s=''):
        ls = s.split("|");
        item = MediaItem.MediaItem();
        item.index = ls[0]
        item.fileName = ls[1]
        item.url = ls[2]
        item.length = ls[3];
        self.addItem(item);



    def test(self):
        item = MediaItem.MediaItem();
        item.index = 0;
        item.fileName = '123'
        item.length = '123'
        item.url = '123'
        self.list.append(item)
        item2 = MediaItem.MediaItem();
        item2.index = 1;
        item2.fileName = '1234'
        item2.length = '1234'
        item2.url = '1234'
        self.list.append(item2)
        item3 = MediaItem.MediaItem();
        item3.index = 2;
        item3.fileName = '12345'
        item3.length = '12345'
        item3.url = '12345'
        self.list.append(item3)
