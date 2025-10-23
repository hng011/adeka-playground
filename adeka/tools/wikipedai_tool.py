import wikipedia

def search_wikipedia_tool(query: str) -> str:
    """
    Search Wikipedia using the official API and return a summary.
    """
    
    try:
        summary = wikipedia.summary(query, sentences=5, auto_suggest=False)
        return summary.strip()

    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:5]
         
        return (f"Your query '{query}' is ambiguous and could refer to multiple topics. "
                f"Which one did you mean? Some options are: {', '.join(options)}")

    except wikipedia.exceptions.PageError:
        return f"Sorry, I could not find a Wikipedia page for '{query}'."

    except Exception as e:
        return f"An error occurred while fetching data: {e}"