import routines

spikes_ressources = {}

def init_spikes_ressources():
    if spikes_ressources == {}:
        spikes_ressources['up'] = routines.load_png('world/spikes/Spike_up.png')
        spikes_ressources['right'] = routines.load_png('world/spikes/Spike_right.png')
        spikes_ressources['down'] = routines.load_png('world/spikes/Spike_down.png')
        spikes_ressources['left'] = routines.load_png('world/spikes/Spike_left.png')
