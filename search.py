import streamlit as st
import typesense
#from sentence_transformers import SentenceTransformer

try:
    client = typesense.Client({
        'nodes': [{
            'host': 'localhost', # For Typesense Cloud use xxx.a1.typesense.net
            'port': '8108',      # For Typesense Cloud use 443
            'protocol': 'http'   # For Typesense Cloud use https
        }],
        'api_key': 'xyz',
        'connection_timeout_seconds': 2
        })
except ConnectionError as e:
    print('Connection failed')
    es = None

def searchProduct(input):
    #model = SentenceTransformer("all-mpnet-base-v2")
    #input_vector = model.encode(input)

    query = {
        "q": input,
        "query_by": "DescriptionVector",
        "exclude_fields": "DescriptionVector"
    }

    res = client.collections['products'].documents.search(query)
    result = res["hits"]
    return result

def main():
    st.title("Product Search")

    search = st.text_input("Search for a product")

    if st.button("Search"):
        if search:
            result = searchProduct(search)
            st.subheader("Search Results")
            for res in result:
                with st.container():
                    if 'document' in res:
                        try:
                            st.header(f"{res['document']['ProductName']}")
                        except Exception as e:
                            print(e)

                        try:
                            st.write(f"{res['document']['Description']}")
                        except Exception as e:
                            print(e)
                        
                        st.divider()

if __name__ == "__main__":
    main()