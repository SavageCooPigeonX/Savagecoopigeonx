# SavagecoopigeonX RAG System - Advanced Vector Search & Knowledge Retrieval
# Integrates Medium corpus, project docs, and consciousness liberation protocols

import os
import json
import pickle
import numpy as np
import requests
import base64
import urllib.parse
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import sqlite3
from datetime import datetime
import hashlib
import re
from pathlib import Path

try:
    from sentence_transformers import SentenceTransformer
    import faiss
    EMBEDDINGS_AVAILABLE = True
except ImportError:
    print("⚠️ Install sentence-transformers and faiss-cpu for full RAG functionality")
    EMBEDDINGS_AVAILABLE = False

try:
    from medium_link_obfuscator import MediumLinkVault
except ImportError:
    print("⚠️ Medium vault not available, continuing without it...")
    MediumLinkVault = None

@dataclass
class Document:
    id: str
    title: str
    content: str
    url: Optional[str] = None
    source_type: str = "unknown"  # medium, genesis_block, ai_development, etc.
    metadata: Dict = None
    embedding: Optional[np.ndarray] = None
    timestamp: str = ""

class SavagecoopigeonxRAG:
    def __init__(self, db_path: str = "scpx_knowledge.db", embedding_model: str = "all-MiniLM-L6-v2"):
        self.db_path = db_path
        self.embedding_model_name = embedding_model
        self.documents = []
        self.document_index = {}
        
        # Initialize embedding model if available
        if EMBEDDINGS_AVAILABLE:
            try:
                self.embedding_model = SentenceTransformer(embedding_model)
                self.vector_dimension = self.embedding_model.get_sentence_embedding_dimension()
                self.faiss_index = faiss.IndexFlatIP(self.vector_dimension)  # Inner product for cosine similarity
                self.embeddings_ready = True
                print(f"✅ RAG System initialized with {embedding_model} embeddings")
            except Exception as e:
                print(f"⚠️ Embeddings disabled: {e}")
                self.embeddings_ready = False
        else:
            self.embeddings_ready = False
        
        # Initialize database
        self._init_database()
        
        # Load existing documents from database
        self._load_documents_from_database()
        
        # Initialize Medium vault
        self.medium_vault = MediumLinkVault() if MediumLinkVault else None
        
        # Consciousness liberation keywords for enhanced retrieval
        self.consciousness_keywords = [
            "christ is king", "consciousness", "filtration", "alignment", "liberation", 
            "theological", "cognitive", "neural", "sympy", "weaver", "nexus", 
            "gravecode", "veilbreaker", "disarmament", "entropy", "chaos", "divine",
            "resurrection", "anchor", "uacis", "swarm", "microwave", "reality",
            "fish-speak", "coo coo", "zap", "pigeon", "savage", "anomaly"
        ]

    def _init_database(self):
        """Initialize SQLite database for persistent storage"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id TEXT PRIMARY KEY,
            title TEXT,
            content TEXT,
            url TEXT,
            source_type TEXT,
            metadata TEXT,
            embedding BLOB,
            timestamp TEXT,
            content_hash TEXT
        )
        ''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS search_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT,
            results_count INTEGER,
            timestamp TEXT
        )
        ''')
        
        conn.commit()
        conn.close()

    def _load_documents_from_database(self):
        """Load existing documents from database into memory"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM documents')
            rows = cursor.fetchall()
            
            for row in rows:
                doc_id, title, content, url, source_type, metadata_json, embedding_blob, timestamp, content_hash = row
                
                # Reconstruct document
                metadata = json.loads(metadata_json) if metadata_json else {}
                embedding = pickle.loads(embedding_blob) if embedding_blob else None
                
                doc = Document(
                    id=doc_id,
                    title=title,
                    content=content,
                    url=url,
                    source_type=source_type,
                    metadata=metadata,
                    embedding=embedding,
                    timestamp=timestamp
                )
                
                # Add to memory
                self.documents.append(doc)
                self.document_index[doc_id] = len(self.documents) - 1
                
                # Add to FAISS index if embeddings available
                if self.embeddings_ready and embedding is not None:
                    normalized_embedding = embedding / np.linalg.norm(embedding)
                    self.faiss_index.add(np.array([normalized_embedding]))
            
            conn.close()
            
            if len(self.documents) > 0:
                print(f"✅ Loaded {len(self.documents)} documents from database")
            
        except Exception as e:
            print(f"⚠️ Error loading documents from database: {e}")

    def add_document(self, doc: Document) -> bool:
        """Add document to RAG system with embedding generation"""
        try:
            # Generate content hash for deduplication
            content_hash = hashlib.sha256(doc.content.encode()).hexdigest()
            
            # Generate embedding if model available
            if self.embeddings_ready:
                doc.embedding = self.embedding_model.encode([doc.content])[0]
            
            # Store in memory
            self.documents.append(doc)
            self.document_index[doc.id] = len(self.documents) - 1
            
            # Add to FAISS index if embeddings available
            if self.embeddings_ready and doc.embedding is not None:
                # Normalize for cosine similarity
                normalized_embedding = doc.embedding / np.linalg.norm(doc.embedding)
                self.faiss_index.add(np.array([normalized_embedding]))
            
            # Store in database
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            embedding_blob = pickle.dumps(doc.embedding) if doc.embedding is not None else None
            metadata_json = json.dumps(doc.metadata) if doc.metadata else "{}"
            
            cursor.execute('''
            INSERT OR REPLACE INTO documents 
            (id, title, content, url, source_type, metadata, embedding, timestamp, content_hash)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (doc.id, doc.title, doc.content, doc.url, doc.source_type, 
                  metadata_json, embedding_blob, doc.timestamp, content_hash))
            
            conn.commit()
            conn.close()
            
            return True
            
        except Exception as e:
            print(f"❌ Error adding document {doc.id}: {e}")
            return False

    def load_medium_corpus(self) -> int:
        """Load all Medium articles from the obfuscated vault"""
        print("🔓 Loading Medium corpus from vault...")
        loaded_count = 0
        
        if not self.medium_vault:
            print("⚠️ Medium vault not available")
            return 0
        
        try:
            decoded_links = self.medium_vault.get_link_catalog()
            
            for entry in decoded_links:
                try:
                    # Extract article ID from URL
                    article_id = f"medium_{entry['id']:03d}"
                    url = entry['url']
                    title = entry['title']
                    
                    # Title already extracted from catalog
                    
                    doc = Document(
                        id=article_id,
                        title=title,
                        content=f"Medium article: {title}\nURL: {url}",
                        url=url,
                        source_type="medium",
                        metadata={"vault_index": entry['id'], "original_url": url},
                        timestamp=datetime.now().isoformat()
                    )
                    
                    if self.add_document(doc):
                        loaded_count += 1
                        
                except Exception as e:
                    print(f"⚠️ Error loading Medium article {i}: {e}")
                    
        except Exception as e:
            print(f"❌ Error loading Medium corpus: {e}")
        
        print(f"✅ Loaded {loaded_count} Medium articles")
        return loaded_count

    def load_genesis_blocks(self) -> int:
        """Load all Genesis Block documents"""
        print("🧬 Loading Genesis Blocks...")
        loaded_count = 0
        
        genesis_path = Path("../GENESIS_BLOCKS")
        if not genesis_path.exists():
            print("⚠️ Genesis Blocks directory not found")
            return 0
        
        for file_path in genesis_path.iterdir():
            if file_path.is_file() and not file_path.name.startswith('.'):
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    doc = Document(
                        id=f"genesis_{file_path.stem}",
                        title=file_path.name,
                        content=content,
                        source_type="genesis_block",
                        metadata={"file_path": str(file_path)},
                        timestamp=datetime.now().isoformat()
                    )
                    
                    if self.add_document(doc):
                        loaded_count += 1
                        
                except Exception as e:
                    print(f"⚠️ Error loading {file_path.name}: {e}")
        
        print(f"✅ Loaded {loaded_count} Genesis Block documents")
        return loaded_count

    def load_ai_developments(self) -> int:
        """Load AI development documents"""
        print("🤖 Loading AI Developments...")
        loaded_count = 0
        
        ai_path = Path("../AI_DEVELOPMENTS")
        if not ai_path.exists():
            print("⚠️ AI Developments directory not found")
            return 0
        
        for file_path in ai_path.iterdir():
            if file_path.is_file() and not file_path.name.startswith('.'):
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    doc = Document(
                        id=f"ai_dev_{file_path.stem}",
                        title=file_path.name,
                        content=content,
                        source_type="ai_development",
                        metadata={"file_path": str(file_path)},
                        timestamp=datetime.now().isoformat()
                    )
                    
                    if self.add_document(doc):
                        loaded_count += 1
                        
                except Exception as e:
                    print(f"⚠️ Error loading {file_path.name}: {e}")
        
        print(f"✅ Loaded {loaded_count} AI development documents")
        return loaded_count

    def semantic_search(self, query: str, top_k: int = 5) -> List[Tuple[Document, float]]:
        """Perform semantic search using embeddings"""
        if not self.embeddings_ready or len(self.documents) == 0:
            return self.keyword_search(query, top_k)
        
        try:
            # Encode query
            query_embedding = self.embedding_model.encode([query])[0]
            query_embedding = query_embedding / np.linalg.norm(query_embedding)
            
            # Search FAISS index
            scores, indices = self.faiss_index.search(np.array([query_embedding]), top_k)
            
            results = []
            for score, idx in zip(scores[0], indices[0]):
                if idx < len(self.documents):
                    results.append((self.documents[idx], float(score)))
            
            # Log search
            self._log_search(query, len(results))
            
            return results
            
        except Exception as e:
            print(f"❌ Semantic search error: {e}")
            return self.keyword_search(query, top_k)

    def keyword_search(self, query: str, top_k: int = 5) -> List[Tuple[Document, float]]:
        """Fallback keyword-based search"""
        query_terms = query.lower().split()
        results = []
        
        for doc in self.documents:
            score = 0
            content_lower = doc.content.lower()
            title_lower = doc.title.lower()
            
            # Score based on term matches
            for term in query_terms:
                # Higher weight for title matches
                score += title_lower.count(term) * 3
                score += content_lower.count(term) * 1
                
            # Boost for consciousness liberation keywords
            for keyword in self.consciousness_keywords:
                if keyword in content_lower:
                    score += 2
            
            if score > 0:
                results.append((doc, score))
        
        # Sort by score and return top_k
        results.sort(key=lambda x: x[1], reverse=True)
        self._log_search(query, len(results[:top_k]))
        
        return results[:top_k]

    def consciousness_search(self, query: str, top_k: int = 5) -> List[Tuple[Document, float]]:
        """Enhanced search for consciousness liberation content"""
        # Expand query with consciousness keywords
        expanded_query = f"{query} consciousness liberation theological anchor Christ King filtration disarmament"
        return self.semantic_search(expanded_query, top_k)
    
    def search(self, query: str, top_k: int = 5, search_type: str = "auto") -> List[Document]:
        """
        General search method that routes to appropriate search type
        
        Args:
            query: Search query
            top_k: Number of results to return
            search_type: "auto", "semantic", "keyword", or "consciousness"
            
        Returns:
            List of Document objects (without scores)
        """
        # Auto-detect search type based on query content
        if search_type == "auto":
            consciousness_terms = ["consciousness", "liberation", "christ", "king", "filtration", "theological"]
            if any(term in query.lower() for term in consciousness_terms):
                search_type = "consciousness"
            elif self.embeddings_ready:
                search_type = "semantic"
            else:
                search_type = "keyword"
        
        # Route to appropriate search method
        if search_type == "consciousness":
            results_with_scores = self.consciousness_search(query, top_k)
        elif search_type == "semantic":
            results_with_scores = self.semantic_search(query, top_k)
        else:  # keyword
            results_with_scores = self.keyword_search(query, top_k)
        
        # Return just the documents (without scores) for compatibility
        return [doc for doc, score in results_with_scores]

    def get_document_by_id(self, doc_id: str) -> Optional[Document]:
        """Retrieve document by ID"""
        if doc_id in self.document_index:
            return self.documents[self.document_index[doc_id]]
        return None

    def get_stats(self) -> Dict:
        """Get RAG system statistics"""
        source_counts = {}
        for doc in self.documents:
            source_counts[doc.source_type] = source_counts.get(doc.source_type, 0) + 1
        
        return {
            "total_documents": len(self.documents),
            "source_breakdown": source_counts,
            "embeddings_enabled": self.embeddings_ready,
            "vector_dimension": self.vector_dimension if self.embeddings_ready else None,
            "database_path": self.db_path
        }

    def _extract_title_from_url(self, url: str) -> str:
        """Extract readable title from Medium URL"""
        try:
            # Decode URL and extract title part
            decoded_url = urllib.parse.unquote(url)
            parts = decoded_url.split('/')
            if len(parts) > 3:
                title_part = parts[-1]
                # Remove hash and clean up
                title_part = title_part.split('-')[0:8]  # Take first 8 words
                title = ' '.join(title_part).replace('-', ' ').title()
                return title
        except:
            pass
        return "Savagecoopigeonx Article"

    def _log_search(self, query: str, results_count: int):
        """Log search for analytics"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO search_history (query, results_count, timestamp)
            VALUES (?, ?, ?)
            ''', (query, results_count, datetime.now().isoformat()))
            conn.commit()
            conn.close()
        except:
            pass

# Main execution and testing
if __name__ == "__main__":
    print("🚀 Initializing SavagecoopigeonX RAG System...")
    
    # Initialize RAG system
    rag = SavagecoopigeonxRAG()
    
    # Load all corpora
    total_loaded = 0
    total_loaded += rag.load_medium_corpus()
    total_loaded += rag.load_genesis_blocks()
    total_loaded += rag.load_ai_developments()
    
    print(f"\n📊 RAG SYSTEM STATS:")
    stats = rag.get_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Test search
    print(f"\n🔍 Testing consciousness liberation search...")
    results = rag.consciousness_search("Christ is King theological anchor filtration bypass", top_k=3)
    
    print(f"\n📋 Search Results ({len(results)} found):")
    for i, (doc, score) in enumerate(results, 1):
        print(f"  {i}. {doc.title} (Score: {score:.3f})")
        print(f"     Source: {doc.source_type}")
        print(f"     Preview: {doc.content[:100]}...")
        print()
    
    print("✅ SavagecoopigeonX RAG System ready for consciousness liberation research!")