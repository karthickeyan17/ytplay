
def format_duration(seconds:int)->str:
    hours , rem = divmod(seconds,3600)
    minutes , seconds = divmod(rem , 60)

    if hours:
        return f"{hours}:{minutes}:{seconds}"
    return f"{minutes}:{seconds}"

def format_views(views:int)->str:
    if views >= 1_000_000_000 :
        return f"{views / 1_000_000_000:.1f}B"
    if views >= 1_000_000 :
        return f"{views / 1_000_000:.1f}M"
    if views >= 1_000 :
        return f"{views / 1_000:.1f}K"
    return str(views)
