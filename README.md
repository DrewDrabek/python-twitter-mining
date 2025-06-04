# python-twitter-mining


### TODO List for `PythonStreamer` Class

1. **Fix `on_status` Placement**  
   - Move `on_status` to a separate `CustomStreamListener` class since it belongs to the listener, not the streamer.

2. **Complete `start_stream` Method**  
   - Ensure the `start_stream` method initializes the stream with the correct listener and starts it asynchronously.  
   - Handle exceptions (e.g., network errors or API rate limits).

3. **Add a `stop_stream` Method**  
   - Implement logic to stop the stream gracefully if needed.

4. **Add Error Handling**  
   - Handle cases where the stream fails or receives invalid data.

5. **Refactor Initialization**  
   - Remove `stream_listener` from the constructor and dynamically create it within the class.

6. **Add Helper Methods**  
   - Add methods to retrieve tweets from the dictionary (e.g., `get_tweets()`).  
   - Add methods to clear the dictionary or reset the tweet count.

---

### TODO List for Other Classes

#### 1. **CustomStreamListener**  
- **Purpose**: Handle incoming tweets and stop the stream when the maximum number of tweets is reached.  
- **Tasks**:  
  1. Create a class that inherits from `StreamListener`.  
  2. Implement the `on_status` method to process tweets and add them to the dictionary.  
  3. Implement error handling methods like `on_error` and `on_exception`.

#### 2. **StreamManager**  
- **Purpose**: Manage multiple `PythonStreamer` instances and provide a centralized interface for creating, starting, and stopping streams.  
- **Tasks**:  
  1. Create a singleton-like class to manage all active streams.  
  2. Implement a method to dynamically create new `PythonStreamer` instances.  
  3. Add methods to start and stop streams for specific keywords.  
  4. Add a method to list all active streams.

#### 3. **CLI Interface**  
- **Purpose**: Provide a user-friendly way to interact with the `StreamManager` and manage listeners.  
- **Tasks**:  
  1. Implement a menu-driven CLI for creating, starting, and stopping listeners.  
  2. Add input validation for keywords and maximum tweet counts.  
  3. Display the status of active streams (e.g., number of tweets collected).

---

### Suggested Workflow

1. **Refactor `PythonStreamer`**  
   - Move `on_status` to `CustomStreamListener`.  
   - Complete the `start_stream` and `stop_stream` methods.

2. **Implement `CustomStreamListener`**  
   - Focus on handling tweets and stopping the stream when needed.

3. **Build `StreamManager`**  
   - Add logic to manage multiple `PythonStreamer` instances.

4. **Create CLI**  
   - Add user interaction for creating and managing streams.
