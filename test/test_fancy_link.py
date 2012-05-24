# vim: set fileencoding=utf-8 :

from tiddlywebplugins.wikklytextrender import render
from tiddlyweb.model.tiddler import Tiddler

link = 'http://➔.ws/ෟ, ' # utf-8
ulink = link.decode('utf-8')

def test_fancy_link():
    tiddler = Tiddler('jrbl', 'bug')
    tiddler.text = ulink

    html = render(tiddler, {})
    print html
