# rec hottest item to user
# -*- coding:utf8 -*-

from operator import itemgetter

def hottest(user_item, top_k):
    item_user = {}
    item_n = {}
    for uid, ilist in user_item.iteritems():
        for iid in ilist:
            ulist = item_user.setdefault(iid, set([]))
            ulist.add(uid)
    for iid, ulist in item_user.iteritems():
        item_n[iid] = len(ulist)
    hot = sorted(item_n.items(), key=itemgetter(1), reverse=True)[:top_k]
    return [k for k,v in hot]
