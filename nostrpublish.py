# Libraries
import time
from pynostr.event import Event
from pynostr.relay_manager import RelayManager
from pynostr.key import PrivateKey

# Relays
relay_manager = RelayManager(timeout=6)
relay_manager.add_relay("wss://nostr-pub.wellorder.net")
relay_manager.add_relay("wss://relay.damus.io")

def nostrpost(private_key,kind,status,imgurl,input,input_type):
    # # Check for https
    if 'https:' in imgurl.lower() or 'http:' in imgurl.lower():
        imgurl = imgurl
    else:
        imgurl = 'https:' + imgurl
    if type(private_key) is str and 'nsec' in private_key:
        # nsec to hex conversion
        private_object = PrivateKey.from_nsec(private_key)
        private_hex = private_object.hex()
    else:
        private_hex = private_key.hex()

    # Simple Note
    event = Event(
                kind = kind, 
                content = status+' '+imgurl
                )
    
    # Speech to Text Event
    # event = Event(
    #             kind = 65002, 
    #             tags = [
    #                         [ "i", "http://here-and-now.info/audio/rickastley_artists.mp3", "text" ],
    #                         [ "output", "text/plain" ]
    #                     ],
    #             content = ''
    #             )

    # Summarize Event
    # event = Event(
    #               kind = 65003, 
    #               tags = [['i', 'The story of my life is that I try and I fail until I eventually succeed.', 'text']],
    #               content = ''
    #               )

    # Image Event
    # ['EVENT', 
    #  {'id': 'cd4672b1673868216b57c50f302b5ba6cad5e75a7728c604664d9838492237e5', 
    #   'pubkey': '558497db304332004e59387bc3ba1df5738eac395b0e56b45bfb2eb5400a1e39', 
    #   'created_at': 1691110127, 
    #   'kind': 65005, 
    #   'tags': [['i', 'Dramatic+ 8k wallpaper medium shot waist up photo of fearsome young witch wearing intricate robes and silver pauldrons, magic+, high detail, detailed background, detailed eyes, wild hair, wind blown hair, cinematic lighting, masterpiece, best quality, high contrast, soft lighting, backlighting, bloom, light sparkles, chromatic aberration, smooth, sharp focus', 'text'], 
    #            ['params', 'negative_prompt', 'hat, old, child, childlike, 3d, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name'], 
    #            ['params', 'size', '768', '768'], 
    #            ['wss://relay.damus.io', 'wss://relay.snort.social', 'wss://blastr.f7z.xyz', 'wss://nostr.mutinywallet.com', 'wss://relayable.org'], 
    #            ['bid', '5000', '10000']], 
    #            'content': 'Generate a Picture based on the attached prompt', 
    #            'sig': '2ae18593540d2c0eb2f27692279bf5d0f65ecb2c975385e4fe436fd3e44b7baf11a9756ae842d7003ff73496e66c56c3f4f937ebf011703d70d5e6bc91bf6b5e'}]

    # Publish
    event.sign(private_hex)
    relay_manager.publish_event(event)
    relay_manager.run_sync()
    # time.sleep(5) # allow the messages to send
    print('Event Published')
    return "Event Published"

if __name__ == '__main__':
    kind = 1
    status = 'This is the way'
    imgurl = 'https://i.giphy.com/media/d2W7eZX5z62ziqdi/200.gif'
    # private_key = PrivateKey()
    # print(private_key.bech32())
    private_key = 'nsec153vkyspeahug9ezchh7f008ckkspfl67c9l6msc37nxmvds5pwlsnzxdl4'
    nostrpost(private_key,kind,status,imgurl,None,None)