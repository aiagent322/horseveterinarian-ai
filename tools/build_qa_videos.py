import html
def render(d):
    by={v['youtube_id']:v for v in d['videos']}
    out={}
    for slug,ids in d['pages'].items():
        cards=[]
        for i in ids:
            v=by[i]; t=html.escape(v['title'],quote=True); pub=html.escape(v['publisher'])
            note=' · commercial channel' if v.get('commercial_note') else ''
            cards.append('''<div class="article-video"><div class="video-frame"><div class="vid-facade" data-vid="%s" data-title="%s" role="button" tabindex="0" aria-label="Play: %s"><img src="https://img.youtube.com/vi/%s/hqdefault.jpg" alt="%s" width="480" height="360" loading="lazy" decoding="async"><div class="vid-play" aria-hidden="true"><svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg></div></div></div><div class="video-caption"><span class="video-cat">🎥 Colic</span><div class="video-text">%s</div><div class="video-by">%s%s</div></div></div>'''%(i,t,t,i,t,t,pub,note))
        out[slug]=cards
    return out
