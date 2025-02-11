from util import hook, database, http, formatting
import random

# RATINGS
# .RATE INFINITY BATTLESTATION 8/10

# .BS WOULD DISPLAY RATING AND TOTAL VOTES
#TYPE, NICK, VOTES, VOTERS

### Battlestations
@hook.command(autohelp=False)
def battlestation(inp, nick=None, conn=None, chan=None,db=None, notice=None):
    "battlestation <url | @ person> -- shows a user's Battlestation."
    if inp:
        if  "http" in inp:
            database.set(db,'users','battlestation',inp.strip(),'nick',nick)
            notice("Saved your battlestation.")
            return
        elif 'del' in inp:
            database.set(db,'users','battlestation','','nick',nick)
            notice("Deleted your battlestation.")
            return
        else:
            if '@' in inp: nick = inp.split('@')[1].strip()
            else: nick = inp.strip()

    result = database.get(db,'users','battlestation','nick',nick)
    if result: 
        return '{}: {}'.format(nick,result)
    else: 
        if not '@' in inp: notice(battlestation.__doc__)
        return 'No battlestation saved for {}.'.format(nick)

### Desktops
@hook.command(autohelp=False)
def desktop(inp, nick=None, conn=None, chan=None,db=None, notice=None):
    "desktop http://url.to/desktop | @ nick -- Shows a user's Desktop."
    if inp:
        if  "http" in inp:
            database.set(db,'users','desktop',inp.strip(),'nick',nick)
            notice("Saved your desktop.")
            return
        elif 'del' in inp:
            database.set(db,'users','desktop','','nick',nick)
            notice("Deleted your desktop.")
            return
        else:
            if '@' in inp: nick = inp.split('@')[1].strip()
            else: nick = inp.strip()

    result = database.get(db,'users','desktop','nick',nick)
    if result: 
        return '{}: {}'.format(nick,result)
    else: 
        if not '@' in inp: notice(desktop.__doc__)
        return 'No desktop saved for {}.'.format(nick)
        

### Greeting
@hook.command('intro', autohelp=False)
@hook.command(autohelp=False)
def greeting(inp, nick=None, conn=None, chan=None,db=None, notice=None):
    "greet <message | @ person> -- Shows a user's Greeting."
    try:
        if not inp or '@' in inp:
            if '@' in inp: nick = inp.split('@')[1].strip()
            result = database.get(db,'users','greeting','nick',nick)
            if result: 
                return '{}: {}'.format(nick,result)
            else: 
                if not '@' in inp: notice(greeting.__doc__)
                return 'No greeting saved for {}.'.format(nick)
        elif 'del' in inp:
            database.set(db,'users','greeting','','nick',nick)
            notice("Deleted your greeting.")
        else:
            database.set(db,'users','greeting','{} '.format(inp.strip().replace("'","").encode('utf8')),'nick',nick)
            notice("Saved your greeting.")
        return
    except: return "Uwaaahh~~?"


### Waifu & Husbando
@hook.command(autohelp=False)
def waifu(inp, nick=None, conn=None, chan=None,db=None, notice=None):
    "waifu <waifu | @ person> -- Shows a user's Waifu or Husbando."

    if not inp or '@' in inp:
        if '@' in inp: nick = inp.split('@')[1].strip()
        result = database.get(db,'users','waifu','nick',nick)
        if result: 
            return '{}: {}'.format(nick,result)
        else: 
            if not '@' in inp: notice(waifu.__doc__)
            return 'No waifu saved for {}.'.format(nick)
    elif 'del' in inp:
        database.set(db,'users','waifu','','nick',nick)
        notice("Deleted your waifu.")
    else:
        database.set(db,'users','waifu','{} '.format(inp.strip().encode('utf8')),'nick',nick)
        notice("Saved your waifu.")
    return


@hook.command(autohelp=False)
def husbando(inp, nick=None, conn=None, chan=None,db=None, notice=None):
    "husbando <husbando | @ person> -- Shows a user's husbando or Husbando."

    if not inp or '@' in inp:
        if '@' in inp: nick = inp.split('@')[1].strip()
        result = database.get(db,'users','husbando','nick',nick)
        if result: 
            return '{}: {}'.format(nick,result)
        else: 
            if not '@' in inp: notice(husbando.__doc__)
            return 'No husbando saved for {}.'.format(nick)
    elif 'del' in inp:
        database.set(db,'users','husbando','','nick',nick)
        notice("Deleted your husbando.")
    else:
        database.set(db,'users','husbando','{} '.format(inp.strip().encode('utf8')),'nick',nick)
        notice("Saved your husbando.")
    return

@hook.command(autohelp=False)
def imouto(inp, nick=None, conn=None, chan=None,db=None, notice=None):
    "imouto <imouto | @ person> -- Shows a user's imouto or Husbando."

    if not inp or '@' in inp:
        if '@' in inp: nick = inp.split('@')[1].strip()
        result = database.get(db,'users','imouto','nick',nick)
        if result: 
            return '{}: {}'.format(nick,result)
        else: 
            if not '@' in inp: notice(imouto.__doc__)
            return 'No imouto saved for {}.'.format(nick)
    elif 'del' in inp:
        database.set(db,'users','imouto','','nick',nick)
        notice("Deleted your imouto.")
    else:
        database.set(db,'users','imouto','{} '.format(inp.strip().encode('utf8')),'nick',nick)
        notice("Saved your imouto.")
    return

@hook.command(autohelp=False)
def daughteru(inp, nick=None, conn=None, chan=None,db=None, notice=None):
    "daughteru <daughteru | @ person> -- Shows a user's daughteru."

    if not inp or '@' in inp:
        if '@' in inp: nick = inp.split('@')[1].strip()
        result = database.get(db,'users','daughteru','nick',nick)
        if result: 
            return '{}: {}'.format(nick,result)
        else: 
            if not '@' in inp: notice(imouto.__doc__)
            return 'No daughteru saved for {}.'.format(nick)
    elif 'del' in inp:
        database.set(db,'users','daughteru','','nick',nick)
        notice("Deleted your daughteru.")
    else:
        database.set(db,'users','daughteru','{} '.format(inp.strip().encode('utf8')),'nick',nick)
        notice("Saved your daughteru.")
    return


### Desktops
@hook.command(autohelp=False)
def birthday(inp, nick=None, conn=None, chan=None,db=None, notice=None):
    "birthday <01/01/2001> | <@ person> -- Shows a user's Birthday."

    if not inp or '@' in inp:
        if '@' in inp: nick = inp.split('@')[1].strip()
        result = database.get(db,'users','birthday','nick',nick)
        if result: 
            return '{}: {}'.format(nick,result)
        else: 
            if not '@' in inp: notice(birthday.__doc__)
            return 'No birthday saved for {}.'.format(nick)
    elif 'del' in inp:
        database.set(db,'users','birthday','','nick',nick)
        notice("Deleted your birthday.")
    else:
        database.set(db,'users','birthday','{} '.format(inp.strip()),'nick',nick)
        notice("Saved your birthday.")
    return

@hook.command(autohelp=False)
def horoscope(inp, db=None, notice=None, nick=None):
    """horoscope <sign> [save] -- Get your horoscope."""
    save = False
    database.init(db)
    
    if '@' in inp:
        nick = inp.split('@')[1].strip()
        sign = database.get(db,'users','horoscope','nick',nick)
        if not sign: return "No horoscope sign stored for {}.".format(nick)
    else:
        sign = database.get(db,'users','horoscope','nick',nick)
        if not inp: 
            if not sign:
                notice(horoscope.__doc__)
                return
        else:
            if not sign: save = True
            if " save" in inp: save = True
            sign = inp.split()[0]

    url = "http://my.horoscope.com/astrology/free-daily-horoscope-%s.html" % sign
    try:
        result = http.get_soup(url)
        title = result.find_all('h1', {'class': 'h1b'})[1].text
        horoscopetxt = result.find('div', {'id': 'textline'}).text
    except: return "Could not get the horoscope for {}.".format(sign.encode('utf8'))

    if sign and save: database.set(db,'users','horoscope',sign,'nick',nick)
    
    return u"\x02{}\x02 {}".format(title, horoscopetxt)


@hook.command(autohelp=False)
def homescreen(inp, nick=None, conn=None, chan=None,db=None, notice=None):
    "homescreen <url | @ person> -- Shows a user's homescreen."
    if "http" in inp:
        database.set(db,'users','homescreen',inp.strip(),'nick',nick)
        notice("Saved your homescreen.")
        return
    elif 'del' in inp:
        database.set(db,'users','homescreen','','nick',nick)
        notice("Deleted your homescreen.")
        return
    elif not inp:
        homescreen = database.get(db,'users','homescreen','nick',nick)
    else:
        if '@' in inp: nick = inp.split('@')[1].strip()
        else: nick = inp.strip()

    homescreen = database.get(db,'users','homescreen','nick',nick)
    if homescreen:
        return '{}: {}'.format(nick,homescreen)
    else:
        # notice(homescreen.__doc__)
        return 'No homescreen saved for {}.'.format(nick)

@hook.command(autohelp=False)
def snapchat(inp, nick=None, conn=None, chan=None,db=None, notice=None):
    "snapchat <snapchatname | @ person> -- Shows a user's snapchat name."

    if not inp or '@' in inp:
        if '@' in inp: nick = inp.split('@')[1].strip()
        result = database.get(db,'users','snapchat','nick',nick)
        if result: 
            return '{}: {}'.format(nick,result)
        else: 
            if not '@' in inp: notice(snapchat.__doc__)
            return 'No snapchat saved for {}.'.format(nick)
    elif 'del' in inp:
        database.set(db,'users','snapchat','','nick',nick)
        notice("Deleted your snapchat.")
    else:
        database.set(db,'users','snapchat','{} '.format(inp.strip().encode('utf8')),'nick',nick)
        notice("Saved your snapchat.")
    return
        
@hook.command(autohelp=False)
def myanime(inp, nick=None, conn=None, chan=None,db=None, notice=None):
    "myanime <mal name | @ person> -- Shows a user's myanimelist profile."

    if not inp or '@' in inp:
        if '@' in inp: nick = inp.split('@')[1].strip()
        result = database.get(db,'users','mal','nick',nick)
        if result: 
            return '{}: http://myanimelist.net/animelist/{}'.format(nick,result)
        else: 
            if not '@' in inp: notice(mal.__doc__)
            return 'No mal saved for {}.'.format(nick)
    elif 'del' in inp:
        database.set(db,'users','mal','','nick',nick)
        notice("Deleted your mal.")
    else:
        database.set(db,'users','mal','{} '.format(inp.strip().encode('utf8')),'nick',nick)
        notice("Saved your mal.")
    return

@hook.command(autohelp=False)
def mymanga(inp, nick=None, conn=None, chan=None,db=None, notice=None):
    "mymanga <mal name | @ person> -- Shows a user's myanimelist profile."

    if not inp or '@' in inp:
        if '@' in inp: nick = inp.split('@')[1].strip()
        result = database.get(db,'users','mal','nick',nick)
        if result: 
            return '{}: http://myanimelist.net/mangalist/{}'.format(nick,result)
        else: 
            if not '@' in inp: notice(mal.__doc__)
            return 'No mal saved for {}.'.format(nick)
    elif 'del' in inp:
        database.set(db,'users','mal','','nick',nick)
        notice("Deleted your mal.")
    else:
        database.set(db,'users','mal','{} '.format(inp.strip().encode('utf8')),'nick',nick)
        notice("Saved your mal.")
    return

@hook.command(autohelp=False)
def selfie(inp, nick=None, conn=None, chan=None,db=None, notice=None):
    "selfie <url | @ person> -- Shows a user's selfie."
    if inp:
        if  "http" in inp:
            database.set(db,'users','selfie',inp.strip(),'nick',nick)
            notice("Saved your selfie.")
            return
        elif 'del' in inp:
            database.set(db,'users','selfie','','nick',nick)
            notice("Deleted your selfie.")
            return
        else:
            if '@' in inp: nick = inp.split('@')[1].strip()
            else: nick = inp.strip()

    result = database.get(db,'users','selfie','nick',nick)
    if result: 
        return '{}: {}'.format(nick,result)
    else: 
        if not '@' in inp: notice(selfie.__doc__)
        return 'No selfie saved for {}.'.format(nick)

@hook.command(autohelp=False)
def steam(inp, nick=None, conn=None, chan=None,db=None, notice=None):
    "steam <steam | @ person> -- Shows a users steam information."
	
    field_name = 'steam'
    field_title = 'Steam'
    field_description = 'profile link'

    if not inp or '@' in inp:
        if '@' in inp: nick = inp.split('@')[1].strip()
        result = database.get(db,'users',field_name,'nick',nick)
        if result:
            return formatting.output(field_title, ['{}: {}'.format(nick,result)])
        else:
            if not '@' in inp: notice(steam.__doc__)
            return formatting.output(field_title, ['No {} {} saved for {}.'.format(field_title, field_description, nick)])
    elif 'del' in inp:
        database.set(db,'users',field_name,'','nick',nick)
        notice("Deleted your {} {}.".format(field_title, field_description))
    else:
        database.set(db,'users',field_name,'{} '.format(inp.strip().encode('utf8')),'nick',nick)
        notice("Saved your {} {}.".format(field_title, field_description))
    return

@hook.command(autohelp=False)
def xbl(inp, nick=None, conn=None, chan=None,db=None, notice=None):
    "xbl <xbl | @ person> -- Shows a user's Xbox Live ID."
	
    field_name = 'xbl'
    field_title = 'Xbox Live'
    field_description = 'ID'

    if not inp or '@' in inp:
        if '@' in inp: nick = inp.split('@')[1].strip()
        result = database.get(db,'users',field_name,'nick',nick)
        if result:
            return formatting.output(field_title, ['{}: {}'.format(nick,result)])
        else:
            if not '@' in inp: notice(xbl.__doc__)
            return formatting.output(field_title, ['No {} {} saved for {}.'.format(field_title, field_description, nick)])
    elif 'del' in inp:
        database.set(db,'users',field_name,'','nick',nick)
        notice("Deleted your {} {}.".format(field_title, field_description))
    else:
        database.set(db,'users',field_name,'{} '.format(inp.strip().encode('utf8')),'nick',nick)
        notice("Saved your {} {}.".format(field_title, field_description))
    return

@hook.command(autohelp=False)
def psn(inp, nick=None, conn=None, chan=None,db=None, notice=None):
    "psn <psn | @ person> -- Shows a user's Playstation Network ID."
	
    field_name = 'psn'
    field_title = 'PSN'
    field_description = 'Playstation Network ID'

    if not inp or '@' in inp:
        if '@' in inp: nick = inp.split('@')[1].strip()
        result = database.get(db,'users',field_name,'nick',nick)
        if result:
            return formatting.output(field_title, ['{}: {}'.format(nick,result)])
        else:
            if not '@' in inp: notice(psn.__doc__)
            return formatting.output(field_title, ['No {} {} saved for {}.'.format(field_title, field_description, nick)])
    elif 'del' in inp:
        database.set(db,'users',field_name,'','nick',nick)
        notice("Deleted your {} {}.".format(field_title, field_description))
    else:
        database.set(db,'users',field_name,'{} '.format(inp.strip().encode('utf8')),'nick',nick)
        notice("Saved your {} {}.".format(field_title, field_description))
    return

@hook.command(autohelp=False)
def nintendo(inp, nick=None, conn=None, chan=None,db=None, notice=None):
    "nintendo <nintendo | @ person> -- shows a user's Nintendo friend code."
	
    field_name = 'nintendo'
    field_title = 'Nintendo'
    field_description = 'Friend Code'

    if not inp or '@' in inp:
        if '@' in inp: nick = inp.split('@')[1].strip()
        result = database.get(db,'users',field_name,'nick',nick)
        if result:
            return formatting.output(field_title, ['{}: {}'.format(nick,result)])
        else:
            if not '@' in inp: notice(nintendo.__doc__)
            return formatting.output(field_title, ['No {} {} saved for {}.'.format(field_title, field_description, nick)])
    elif 'del' in inp:
        database.set(db,'users',field_name,'','nick',nick)
        notice("Deleted your {} {}.".format(field_title, field_description))
    else:
        database.set(db,'users',field_name,'{} '.format(inp.strip().encode('utf8')),'nick',nick)
        notice("Saved your {} {}.".format(field_title, field_description))
    return

@hook.command(autohelp=False)
def vidya(inp, nick=None, conn=None, chan=None,db=None, notice=None):
    "vidya <vidya | @ person> -- shows a user's video game contacts."
    output = []

    if '@' in inp: nick = inp.split('@')[1].strip()

    fields = {'Steam': 'steam', 'XBL': 'xbl', 'PSN': 'psn', 'Nintendo Friend Code': 'nintendo'}
    output_fields = ['Steam', 'XBL', 'PSN', 'Nintendo Friend Code']
    for field in output_fields:
        result = database.get(db,'users',fields[field],'nick',nick)
        if result:
            output.append('{}: {}'.format(field, result).rstrip())
        else:
            output.append('{}: [N/A]'.format(field))

    return formatting.output('vidya', output)

    ###Old
    #result = unicode(result, "utf8").replace('flight ','')

    # try: sign = db.execute("select horoscope from users where nick=lower(?)", (nick,)).fetchone()[0]
    # except: save = True

    #db.execute("UPSERT INTO users(nick, horoscope) VALUES (?,?)",(nick.lower(), sign,))
    #db.commit()
