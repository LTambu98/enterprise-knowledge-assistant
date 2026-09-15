# Enterprise Knowledge Assistant

Chatbot aziendale che risponde a domande sui documenti interni di un'azienda 
(policy HR, regolamenti, benefit) utilizzando un'architettura RAG 
(Retrieval-Augmented Generation).

## Problema che risolve

Invece di far cercare manualmente informazioni sparse in più PDF aziendali 
(ferie, smart working, benefit, regolamento IT), l'utente può fare una domanda 
in linguaggio naturale e ricevere una risposta basata sul contenuto reale dei documenti.

## Come funziona

1. I documenti vengono suddivisi in chunk e trasformati in embedding
2. Gli embedding vengono salvati in un vector database
3. Alla domanda dell'utente, il sistema recupera i chunk più rilevanti tramite 
   similarity search
4. Un LLM genera la risposta basandosi sul contesto recuperato

## Stack tecnologico

- **Backend**: Python, FastAPI
- **Vector database**: ChromaDB
- **LLM**: [da definire]

## Stato del progetto

🚧 In sviluppo — progetto personale realizzato in preparazione a un colloquio 
come AI Developer.

## Possibili evoluzioni

- Deployment con Docker
- Migrazione su Azure (Azure OpenAI, Azure AI Search)
- Aggiunta di un AI Agent con tool multipli (ricerca documenti, calcolatrice, 
  API HR simulata)
