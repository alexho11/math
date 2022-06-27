import matplotlib.pyplot as plt
import matplotlib.patches as patches
from linear import lin
from tri import tri

ann_list=[]
def plot(p):
    global ann_list
    n=len(p)-1
    pix,piy=tri(p)
    x,y=lin(p)
    l1.set_xdata(x)
    l1.set_ydata(y)
    l2.set_xdata(pix)
    l2.set_ydata(piy)
    for ann in ann_list:
        ann.remove()
    ann_list=[]
    for i in range(n+1):
        ann=plt.annotate('p'+str(i),p[i],(p[i][0]+0.01,p[i][1]+0.01))#annotate
        ann_list.append(ann)
    fig.canvas.draw()
    fig.canvas.flush_events()
    

class DraggablePoints(object):
    def __init__(self, artists, tolerance=5):
        for artist in artists:
            artist.set_picker(tolerance)
        self.artists = artists
        self.x,self.y=0,0
        self.currently_dragging = False
        self.current_artist = None
        self.offset = (0, 0)
        for canvas in set(artist.figure.canvas for artist in self.artists):
            canvas.mpl_connect('button_press_event', self.on_press)
            canvas.mpl_connect('button_release_event', self.on_release)
            canvas.mpl_connect('pick_event', self.on_pick)
            canvas.mpl_connect('motion_notify_event', self.on_motion)

    def on_press(self, event):
        self.currently_dragging = True

    def on_release(self, event):
        self.x=self.current_artist.center[0]
        self.y=self.current_artist.center[1]
        self.currently_dragging = False
        self.current_artist = None
        newp=[]
        for artist in self.artists:
            newp.append(artist.center)
        plot(newp)
        
    def on_pick(self, event):
        if self.current_artist is None:
            self.current_artist = event.artist
            x0, y0 = event.artist.center
            x1, y1 = event.mouseevent.xdata, event.mouseevent.ydata
            self.offset = (x0 - x1), (y0 - y1)

    def on_motion(self, event):
        if not self.currently_dragging:
            return
        if self.current_artist is None:
            return
        dx, dy = self.offset
        self.current_artist.center = event.xdata + dx, event.ydata + dy
        self.current_artist.figure.canvas.draw()

if __name__ == '__main__':
    fig, ax = plt.subplots()
    ax.set(xlim=[0, 1], ylim=[0, 1])

    circles = [patches.Circle((0.32, 0.3), 0.05, fc='r', alpha=0.5),
               patches.Circle((0.3, 0.3), 0.05, fc='b', alpha=0.5),
               patches.Circle((0.1, 0.2), 0.05, fc='b', alpha=0.5),
               patches.Circle((0.5, 0.6), 0.05, fc='b', alpha=0.5),
               ]
    p=[]
    for circ in circles:
        ax.add_patch(circ)
        p.append(circ.center)
    n=len(p)-1
    pix,piy=tri(p)
    x,y=lin(p)
    l1,=plt.plot(x,y,label='linear interpolat')
    l2,=plt.plot(pix,piy,label='trigonometric interpolat')
    ann_list=[]
    for i in range(n+1):
        ann=plt.annotate('p'+str(i),p[i],(p[i][0]+0.01,p[i][1]+0.01))#annotate
        ann_list.append(ann)
    plt.legend()
    plt.show(block=False)

    dr = DraggablePoints(circles)
    plt.show()