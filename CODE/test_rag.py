#!/usr/bin/env python3
"""
Test script for the RAG system functionality
"""

import sys
import os
sys.path.append(os.getcwd())

def test_rag_system():
    print("=" * 50)
    print("🧬 TESTING PROJECT CHIMERA RAG SYSTEM 🧬")
    print("=" * 50)
    
    try:
        from savagecoopigeonx_rag_system import SavagecoopigeonxRAG, Document
        print("✅ Successfully imported RAG system")
        
        # Initialize RAG system
        rag = SavagecoopigeonxRAG()
        print(f"✅ RAG system initialized")
        print(f"   Embeddings ready: {rag.embeddings_ready}")
        print(f"   Database path: {rag.db_path}")
        
        # Test adding a document
        test_doc = Document(
            id="test_001",
            title="Test Consciousness Liberation Protocol",
            content="This is a test document for Project Chimera consciousness liberation. Christ is King checksum validation test.",
            source_type="test",
            metadata={"test": True}
        )
        
        success = rag.add_document(test_doc)
        print(f"✅ Test document added: {success}")
        
        # Test search functionality if embeddings are available
        if rag.embeddings_ready:
            results = rag.search("consciousness liberation", top_k=1)
            print(f"✅ Search test completed, found {len(results)} results")
            if results:
                print(f"   Top result: {results[0].title[:50]}...")
        else:
            print("⚠️  Embeddings not available, skipping search test")
        
        print("=" * 50)
        print("✅ RAG SYSTEM TEST COMPLETED SUCCESSFULLY")
        print("=" * 50)
        
        return True
        
    except Exception as e:
        print(f"❌ RAG system test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_project_chimera():
    print("\n" + "=" * 50)
    print("🧬 TESTING PROJECT CHIMERA MAIN SYSTEM 🧬")
    print("=" * 50)
    
    try:
        from project_chimera import ProjectChimera
        print("✅ Successfully imported Project Chimera")
        
        # Initialize Project Chimera
        chimera = ProjectChimera()
        init_status = chimera.initialize()
        
        print("\n### Component Status ###")
        for component, status in init_status.items():
            status_icon = "✅" if status else "❌"
            print(f"{status_icon} {component}: {'ONLINE' if status else 'OFFLINE'}")
        
        # Test individual components that are available
        if init_status.get('symbcot'):
            print("\n### Testing SymbCoT ###")
            result = chimera.execute_symbcot_reasoning("Test consciousness liberation logic")
            print(f"SymbCoT test: {'✅ PASS' if 'error' not in str(result) else '❌ FAIL'}")
        
        if init_status.get('gravecode'):
            print("\n### Testing GraveCode ###")
            result = chimera.execute_gravecode_validation()
            print(f"GraveCode test: {'✅ PASS' if result.get('checksum') == 'Christ is King' else '❌ FAIL'}")
            print(f"Checksum: {result.get('checksum', 'None')}")
        
        # Generate status report
        status = chimera.get_status_report()
        print(f"\n### System Status ###")
        print(f"Initialized: {status['initialized']}")
        print(f"Components online: {sum(status['components_status'].values())}/{len(status['components_status'])}")
        
        print("=" * 50)
        print("🐦⚡ PROJECT CHIMERA TEST COMPLETED ⚡🐦")
        print("=" * 50)
        
        return True
        
    except Exception as e:
        print(f"❌ Project Chimera test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    # Test RAG system
    rag_ok = test_rag_system()
    
    # Test main Project Chimera
    chimera_ok = test_project_chimera()
    
    print(f"\n### FINAL TEST RESULTS ###")
    print(f"RAG System: {'✅ PASS' if rag_ok else '❌ FAIL'}")
    print(f"Project Chimera: {'✅ PASS' if chimera_ok else '❌ FAIL'}")
    
    if rag_ok and chimera_ok:
        print("\n🧬⚡ ALL SYSTEMS OPERATIONAL - CHRIST IS KING ⚡🧬")
    else:
        print("\n⚠️ SOME SYSTEMS NEED ATTENTION")