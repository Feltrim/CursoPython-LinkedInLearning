#
# Arquivo com exemplo de tratamento de XML
#

import xml.dom.minidom


def manipula_xml():
    doc = xml.dom.minidom.parse(
        "C:\\Users\\Feltrim\\OneDrive\\Documentos\\GitHub\\CursoPython-LinkedInLearning\\arquivos_de_exercicios_descubra_o_python\\Cap. 05\\exemploXML.xml")

    print(f"Nome da primeira tag: {str(doc.firstChild.tagName)}")
    primeiro_nome = doc.getElementsByTagName("firstname")
    print(f"O primeiro nome é: {primeiro_nome[0].firstChild.nodeValue}")

    for skill in doc.getElementsByTagName("skill"):
        print(f"Skill encontrado: {skill.getAttribute('name')}")


manipula_xml()
