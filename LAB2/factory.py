from player import Player
import xml.etree.ElementTree as ET

class PlayerFactory:
    def to_json(self, players):
        '''
            This function should transform a list of Player objects into a list with dictionaries.
        '''
        def player_to_json(player):
            return {"nickname" : player.nickname,
                    "email" : player.email,
                    "date_of_birth" : player.date_of_birth.strftime("%Y-%m-%d"),
                    "xp" : player.xp,
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
                          dct['xp'],
                          dct['class'])

        return [json_to_player(d) for d in list_of_dict]

    def from_xml(self, xml_string):
        '''
            This function should transform a XML string into a list with Player objects.
        '''
        pass

    def to_xml(self, list_of_players):
        '''
            This function should transform a list with Player objects into a XML string.
        '''
        pass

    def from_protobuf(self, binary):
        '''
            This function should transform a binary protobuf string into a list with Player objects.
        '''
        pass

    def to_protobuf(self, list_of_players):
        '''
            This function should transform a list with Player objects intoa binary protobuf string.
        '''
        pass

