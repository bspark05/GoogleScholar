from neo4j.v1 import GraphDatabase, basic_auth


class GS_Neo4j:
    def __init__(self, id, pw):
        self.id = id
        self.pw = pw
        driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth(id, pw))
        self.session = driver.session()
    

#     def startSesseion(self):
#         driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "bspark05"))
#         self.session = driver.session()

    def endSession(self):
        self.session.close()
     
#     def addRef(self, refFrom, refTo):
#         self.session.run("")