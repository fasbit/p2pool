from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['bitcoin']
SHARE_PERIOD = 10 # seconds
CHAIN_LENGTH = 4*24*60*60//10 # shares
REAL_CHAIN_LENGTH = 4*24*60*60//10 # shares
TARGET_LOOKBEHIND = 300 # shares
SPREAD = 30 # blocks
IDENTIFIER = 'fc70035c7a81bc6f'.decode('hex')
PREFIX = '2472ef181efcd37b'.decode('hex')
P2P_PORT = 9333
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = True
WORKER_PORT = 9332
BOOTSTRAP_ADDRS = ' '.split(' ')
#ANNOUNCE_CHANNEL = '#p2pool'
VERSION_CHECK = lambda v: 50700 <= v < 60000 or 60010 <= v < 60100 or 60400 <= v
VERSION_WARNING = lambda v: 'Upgrade Bitcoin to >=0.8.5!' if v < 80500 else None
