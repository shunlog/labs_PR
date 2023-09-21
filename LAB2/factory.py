from player import Player
import xml.etree.ElementTree as ET
from icecream import ic
from proto import player_pb2

class PlayerFactory:
    def to_json(self, players):
        '''
            This function should transform a list of Player objects into a list with dictionaries.
        '''
        def player_to_json(player):
            return {"nickname" : player.nickname,
                    "email" : player.email,
                    "date_of_birth" : player.date_of_birth.strftime("%Y-%m-%d"),
                    "xp" : int(player.xp),
                    "class" : player.cls}

        return [player_to_json(p) for p in players]

    def from_json(self, list_of_dict):
        '''
            This function should transform a list of dictionaries into a list with Player objects.
        '''
        def json_to_player(dct):
            return Player(dct['nickname'],
                          dct['email'],
                          dct['date_of_birth'],
                          int(dct['xp']),
                          dct['class'])

        return [json_to_player(d) for d in list_of_dict]

    def from_xml(self, xml_string):
        '''
            This function should transform a XML string into a list with Player objects.
        '''
        root = ET.fromstring(xml_string)
        ls_of_dict = [{attr.tag: attr.text for attr in pl} for pl in root]

        return self.from_json(ls_of_dict)

    def to_xml(self, list_of_players):
        '''
            This function should transform a list with Player objects into a XML string.
        '''
        root = ET.Element('data')
        for p in list_of_players:
            player = ET.SubElement(root, 'player')

            nickname = ET.SubElement(player, 'nickname')
            nickname.text = p.nickname

            email = ET.SubElement(player, 'email')
            email.text = p.email

            date_of_birth = ET.SubElement(player, 'date_of_birth')
            date_of_birth.text = p.date_of_birth.strftime("%Y-%m-%d")

            xp = ET.SubElement(player, 'xp')
            xp.text = str(p.xp)

            cls = ET.SubElement(player, 'class')
            cls.text = p.cls

        s = ET.tostring(root, encoding='utf8')
        return s

    def from_protobuf(self, binary):
        '''
            This function should transform a binary protobuf string into a list with Player objects.
        '''
        proto_ls = player_pb2.PlayersList()
        proto_ls.ParseFromString(binary)

        class_enum = {0: "Berserk",
                      1: "Tank",
                      3: "Paladin",
                      4: "Mage"}

        ls = []
        for p in proto_ls.player:
            player = Player(p.nickname,
                            p.email,
                            p.date_of_birth,
                            p.xp,
                            class_enum[p.cls])
            ls.append(player)

        return ls


    def to_protobuf(self, list_of_players):
        '''
            This function should transform a list with Player objects intoa binary protobuf string.
        '''
        proto_ls = player_pb2.PlayersList()
        for p in list_of_players:
            proto_ls.player.add(nickname = p.nickname,
                          email = p.email,
                          date_of_birth = p.date_of_birth.strftime("%Y-%m-%d"),
                          xp = int(p.xp),
                          cls = p.cls)

        return proto_ls.SerializeToString()
