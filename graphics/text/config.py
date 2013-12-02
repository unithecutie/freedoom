#
# Copyright (c) 2013
# Contributors to the Freedoom project.  All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of the freedoom project nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
# IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
# OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# ----------------------------------------------------------------------
#
# Configuration file for textgen. This file defines the graphic lumps
# that are generated, and the text to show in each one.
#

white_graphics = {
	'wibp1': 'P1',
	'wibp2': 'P2',
	'wibp3': 'P3',
	'wibp4': 'P4',
	'wicolon': ':',
	'wiminus': '-',

	# TODO: Generate WILV graphics based on level names from DEHACKED lump.

	'cwilv00': 'MAP01', 'cwilv01': 'MAP02', 'cwilv02': 'MAP03',
	'cwilv03': 'MAP04', 'cwilv04': 'MAP05', 'cwilv05': 'MAP06',
	'cwilv06': 'MAP07', 'cwilv07': 'MAP08', 'cwilv08': 'MAP09',
	'cwilv09': 'MAP10',

	'cwilv10': 'MAP11', 'cwilv11': 'MAP12', 'cwilv12': 'MAP13',
	'cwilv13': 'MAP14', 'cwilv14': 'MAP15', 'cwilv15': 'MAP16',
	'cwilv16': 'MAP17', 'cwilv17': 'MAP18', 'cwilv18': 'MAP19',
	'cwilv19': 'MAP20',

	'cwilv20': 'MAP21', 'cwilv21': 'MAP22', 'cwilv22': 'MAP23',
	'cwilv23': 'MAP24', 'cwilv24': 'MAP25', 'cwilv25': 'MAP26',
	'cwilv26': 'MAP27', 'cwilv27': 'MAP28', 'cwilv28': 'MAP29',
	'cwilv29': 'MAP30',

	'cwilv30': 'MAP31', 'cwilv31': 'MAP32',

	'wilv00': 'E1M1', 'wilv01': 'E1M2', 'wilv02': 'E1M3', 'wilv03': 'E1M4',
	'wilv04': 'E1M5', 'wilv05': 'E1M6', 'wilv06': 'E1M7', 'wilv07': 'E1M8',
	'wilv08': 'E1M9',

	'wilv10': 'E2M1', 'wilv11': 'E2M2', 'wilv12': 'E2M3', 'wilv13': 'E2M4',
	'wilv14': 'E2M5', 'wilv15': 'E2M6', 'wilv16': 'E2M7', 'wilv17': 'E2M8',
	'wilv18': 'E2M9',

	'wilv20': 'E3M1', 'wilv21': 'E3M2', 'wilv22': 'E3M3', 'wilv23': 'E3M4',
	'wilv24': 'E3M5', 'wilv25': 'E3M6', 'wilv26': 'E3M7', 'wilv27': 'E3M8',
	'wilv28': 'E3M9',

	'wilv30': 'E4M1', 'wilv31': 'E4M2', 'wilv32': 'E4M3', 'wilv33': 'E4M4',
	'wilv34': 'E4M5', 'wilv35': 'E4M6', 'wilv36': 'E4M7', 'wilv37': 'E4M8',
	'wilv38': 'E4M9',
}

blue_graphics = {
	'm_disopt': 'DISPLAY OPTIONS',
	'm_episod': 'Choose Episode:',
	'm_optttl': 'OPTIONS',
	'm_skill': 'Choose Skill Level:',
}

red_graphics = {
	'm_ngame': 'New Game',
	'm_option': 'Options',
	'm_loadg': 'Load Game',
	'm_saveg': 'Save Game',
	'm_rdthis': 'Read This!',
	'm_quitg': 'Quit Game',

	'm_newg': 'NEW GAME',
	'm_epi1': 'First Episode',
	'm_epi2': 'Second Episode',
	'm_epi3': 'Third Episode',
	'm_epi4': 'Fourth Episode',

	'm_jkill': 'Please don\'t kill me!',
	'm_rough': 'Will this hurt?',
	'm_hurt': 'Bring on the pain.',
	'm_ultra': 'Extreme Carnage',
	'm_nmare': 'INSANITY!',

	'm_lgttl': 'LOAD GAME',
	'm_sgttl': 'SAVE GAME',

	'm_endgam': 'End Game',
	'm_messg': 'Messages:',
	'm_msgoff': 'off',
	'm_msgon': 'on',
	'm_msens': 'Mouse Sensitivity',
	'm_detail': 'Graphic Detail:',
	'm_gdhigh': 'high',
	'm_gdlow': 'low',
	'm_scrnsz': 'Screen Size',

	'm_svol': 'Sound Volume',
	'm_sfxvol': 'Sfx Volume',
	'm_musvol': 'Music Volume',

	'm_disp': 'Display',

	'wif': 'finished',
	'wiostk': 'kills',
	'wiosti': 'items',
	'wiscrt2': 'secret',
	'wiosts': 'scrt',
	'wifrgs': 'frgs',

	'witime': 'Time:',
	'wisucks': 'sucks',
	'wimstt': 'Total:',
	'wipar': 'Par:',
	'wip1': 'P1', 'wip2': 'P2', 'wip3': 'P3', 'wip4': 'P4',
	'wiostf': 'f.',
	'wimstar': 'you',
	'winum0': '0', 'winum1': '1', 'winum2': '2', 'winum3': '3',
	'winum4': '4', 'winum5': '5', 'winum6': '6', 'winum7': '7',
	'winum8': '8', 'winum9': '9',
	'wipcnt': '%',
	'wienter': 'ENTERING',

	'm_pause': 'pause',

	# Extra graphics used in PrBoom's menus. Generate these as well
	# so that when we play in PrBoom the menus look consistent.
	'prboom': 'PrBoom',
	'm_generl': 'General',
	'm_setup': 'Setup',
	'm_keybnd': 'Key Bindings',
	'm_weap': 'Weapons',
	'm_stat': 'Status Bar/HUD',
	'm_auto': 'Automap',
	'm_enem': 'Enemies',
	'm_mess': 'Messages',
	'm_chat': 'Chat Strings',

	'm_horsen': 'horizontal',
	'm_versen': 'vertical',
	'm_loksen': 'mouse look',
	'm_accel': 'acceleration',

	# Extra graphics from SMMU/Eternity Engine:
	'm_about': 'about',
	'm_chatm': 'Chat Strings',
	'm_compat': 'Compatibility',
	'm_demos': 'demos',
	'm_dmflag': 'deathmatch flags',
	'm_etcopt': 'eternity options',
	'm_feat': 'Features',
	'm_gset': 'game settings',
	'm_hud': 'heads up display',
	'm_joyset': 'joysticks',
	'm_ldsv': 'Load/Save',
	'm_menus': 'Menu Options',
	'm_mouse': 'mouse options',
	'm_multi': 'multiplayer',
	'm_player': 'player setup',
	'm_serial': 'serial connection',
	'm_sound': 'sound options',
	'm_status': 'status bar',
	'm_tcpip': 'tcp/ip connection',
	'm_video': 'video options',
	'm_wad': 'load wad',
	'm_wadopt': 'wad options',
}

