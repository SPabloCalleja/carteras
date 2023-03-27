from grobid_client.grobid_client import GrobidClient

if __name__ == "__main__":
    client = GrobidClient(config_path="./config.json")
    client.process("processFulltextDocument", "../Corpus/Cartas", 
                   output="../Corpus/Cartas_XML/", 
                   consolidate_citations=False, 
                   tei_coordinates=True, force=True)
