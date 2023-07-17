# langchainpractice

LangChain es un framework para desarrollar aplicaciones basadas en modelos lingüísticos.
https://python.langchain.com/docs/get_started/introduction.html

## Librerias Necesarias 
```
pip install pypdf
pip install openai
pip install tiktoken
pip install fastapi
pip install "uvicorn[standard]"
pip install python-multipart
```
* Cargar PDF utilizando pypdf en una matriz de documentos, donde cada documento contiene el contenido de la página y los metadatos con el número de página.

## Sobre

cadenas ->
agentes -> manejan modelos
memoria -> persistencia
callbacks -> logs

## Modelos
LLM no mantiene el contexto - chat model

data cn - varias fuentes carga-transforma

one hot encoding vectores con espacio similar dependiendo del contexto

## Formas de interactuar
# Staff
Concatena documentos y prompts. Solo para un documento.
# Refine
Itera entre documentos con el prompt y genera una respuesta. Informacion compactada, solo resumida. Para varios documentos.
# Map Reduce
Informacion extensa. Genera varios documentos resumidos y estos son enviados con el prompt. Muchas peticiones. 
# Map re-rank
Prompts con los documentos y los evalua. Despues la califiacion mas alta es el seleccionado.

Chroma: Almacena los vectores o embedings

RLHF Reinforcement learning from human feedback: Retroalimentacion de varias fuentes. Como redes.