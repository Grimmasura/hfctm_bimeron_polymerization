glyph_dict = {
    'CW_Meron': '\u21BB',
    'CCW_Meron': '\u21BA',
    'LinearBond': '\u23AF',
    'Loop': '\u25EF',
    'HexTile': '\u2394'
}

# Example polymer chain
polymer_chain = ['\u21BB', '\u23AF', '\u21BA', '\u23AF', '\u21BB', '\u23AF', '\u21BA']
print('Polymer Chain:', ' '.join(polymer_chain))

# Example closed loop cluster
loop_cluster = ['\u25EF']
print('Closed Loop Cluster:', ' '.join(loop_cluster))
