class Tree:
    def __init__(self, name, children):
        self.name = name
        self.children = children

    # depth first search
    def path_to_node(self, name, path):
        # found node
        if self.name == name:
            return path + [self.name]
        # leaf node, not found
        elif self.children is None:
            return None
        # keep searching
        else:
            for child in self.children:
                search = child.path_to_node(name, path + [self.name])
                if search is not None:
                    return search

    def distance_between_nodes(self, name1, name2):
        distance1 = self.path_to_node(name1, [])
        distance2 = self.path_to_node(name2, [])
        for index, (lab1, lab2) in enumerate(zip(distance1, distance2)):
            if lab1 != lab2:
                return min(len(distance1), len(distance2)) - index, min(len(distance1), len(distance2))

        return 0, min(len(distance1), len(distance2))

trueTree = Tree('chordata', [
    Tree('Squamata', [
        Tree('Pogona', None),
        Tree('Lamprophis', None),
        Tree('Gekko', [
            Tree('Gekko_japonicus', None)
        ]),
        Tree('Eublepharis_macularius', None),
        Tree('Xenopeltis_unicolor', None),
        Tree('Python_bivittatus', None),
        Tree('Scincella_lateralis', None),
        Tree('Elgaria_multicarinata', None),
        Tree('Candoia_aspera', None),
        Tree('Anolis_sagrei', None),
        Tree('Thamnophis', [
            Tree('Thamnophis_sirtalis', None),
            Tree('Thamnophis_elegans', None),
            Tree('Thamnophis_couchii', None)
        ]),
        Tree('Viperidae', [
            Tree('Protobothrops_mucrosquamatus', None),
            Tree('Agkistrodon_piscivorus', None)
        ]),
        Tree('Sceloporus_undulatus', None)
    ]),
    Tree('Aves', [
        Tree('Pelecaniformes', [
            Tree('Egretta', None),
            Tree('Nipponia_nippon', None),
            Tree('Phaethon_lepturus', None),
            Tree('Phalacrocorax_carbo', None)
        ]),
        Tree('Antrostomus_carolinensis', None),
        Tree('Pterocles_gutturalis', None),
        Tree('Pterocles_namaqua', None),
        Tree('Buceros_rhinoceros', None),
        Tree('Tauraco_erythrolophus', None),
        Tree('Picoides_pubescens', None),
        Tree('Tinamus_guttatus', [
            Tree('Coraciiformes', [
                Tree('Leptosomus_discolor', None),
                Tree('Merops_nubicus', None)
            ])
        ]),
        Tree('Colius_striatus', None),
        Tree('Apaloderma_vittatum', None),
        Tree('Tyto_alba1', None),
        Tree('Tyto_alba2', None),
        Tree('Cuculus_canorus', None),
        Tree('Cariama_cristata', [
            Tree('Gruiformes', [
                Tree('Balearica_regulorum', None),
                Tree('Chlamydotis_macqueenii', None),
                Tree('Eurypyga_helias', None),
                Tree('Mesitornis_unicolor', None)
            ]),
            Tree('Charadriiformes', [
                Tree('Calidris_pugnax', None),
                Tree('Charadrius_vociferus', None)
            ])
        ]),
        Tree('Gavia_stellata', None),
        Tree('Fulmarus_glacialis', [
            Tree('Opisthocomiformes', [
                Tree('Opisthocomidae', [
                    Tree('Opisthocomus', [
                        Tree('Opisthocomus_hoazin1', None),
                        Tree('Opisthocomus_hoazin2', None)
                    ])
                ])
            ])
        ]),
        Tree('Psittaciformes', [
            Tree('Nestor_notabilis', None),
            Tree('Melopsittacus_undulatus', None)
        ]),
        Tree('Spheniscidae', [
            Tree('Pygoscelis_adeliae', None),
            Tree('Aptenodytes_forsteri', None)
        ]),
        Tree('Passeriformes', [
            Tree('Manacus_vitellinus', None),
            Tree('Corvus', [
                Tree('Corvus_cornix', None),
                Tree('Corvus_brachyrhynchos', None)
            ]),
            Tree('Ficedula_albicollis', None),
            Tree('Taeniopygia_guttata', None),
            Tree('Acanthisitta_chloris', None),
            Tree('Geospiza_fortis', None),
            Tree('Zonotrichia_albicollis', None),
            Tree('Sturnus_vulgaris', None),
            Tree('Paridae', [
                Tree('Pseudopodoces_humilis', None),
                Tree('Parus_major', None)
            ]),
            Tree('Serinus_canaria', None)
        ]),
        Tree('Phasianidae', [
            Tree('Coturnix_japonica', None),
            Tree('Meleagris_gallopavo', None),
            Tree('Gallus_gallus', None)
        ]),
        Tree('Accipitridae', [
            Tree('Haliaeetus', [
                Tree('Haliaeetus_leucocephalus1', None),
                Tree('Haliaeetus_leucocephalus2', None),
                Tree('Haliaeetus_albicilla', None)
            ]),
            Tree('Aquila_chrysaetos', None)
        ]),
        Tree('Falco', [
            Tree('Falco_cherrug', None),
            Tree('Falco_peregrinus', None)
        ]),
        Tree('Columba_livia', [
            Tree('Apodiformes', [
                Tree('Calypte_anna', None),
                Tree('Chaetura_pelagica', None)
            ])
        ]),
        Tree('Anatidae', [
            Tree('Anser_cygnoides', None),
            Tree('Anas_platyrhynchos', None)
        ]),
        Tree('Struthio_camelus', None),
        Tree('Apteryx_australis_mantelli', None)
    ]),
    Tree('Crocodylia', [
        Tree('Gavialis_gangeticus', None),
        Tree('Crocodylus_porosus', None),
        Tree('Alligator', [
            Tree('Alligator_sinensis', None),
            Tree('Alligator_mississippiensis', None)
        ])
    ]),
    Tree('Testudines', [
        Tree('Pelusios_castaneus', None),
        Tree('Sternotherus_odoratus', None),
        Tree('Pelodiscus_sinensis', [
            Tree('Emydidae', [
                Tree('Terrapene_carolina', None),
                Tree('Chrysemys_picta', None)
            ])
        ]),
        Tree('Chelydra_serpentina', None),
        Tree('Chelonia_mydas', None)
    ])
])
