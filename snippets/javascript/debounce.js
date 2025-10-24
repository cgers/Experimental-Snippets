/**
 * Example Snippet: Debounce Function
 * 
 * This snippet demonstrates a debounce utility function that delays function execution
 * until after a specified wait period has elapsed since the last call.
 * 
 * Source: AI-generated example
 * 
 * Usage:
 *   const debouncedSearch = debounce(searchFunction, 300);
 *   inputElement.addEventListener('input', debouncedSearch);
 */

/**
 * Creates a debounced function that delays invoking func until after wait milliseconds
 * have elapsed since the last time the debounced function was invoked.
 * 
 * @param {Function} func - The function to debounce
 * @param {number} wait - The number of milliseconds to delay
 * @returns {Function} The debounced function
 */
function debounce(func, wait) {
    let timeoutId;
    
    return function debounced(...args) {
        const context = this;
        
        // Clear the previous timeout
        clearTimeout(timeoutId);
        
        // Set a new timeout
        timeoutId = setTimeout(() => {
            func.apply(context, args);
        }, wait);
    };
}

// Example usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = debounce;
}

// Example: Debounced search function
const searchAPI = (query) => {
    console.log(`Searching for: ${query}`);
    // Simulated API call
};

const debouncedSearch = debounce(searchAPI, 300);

// These calls will be debounced - only the last one will execute after 300ms
// debouncedSearch('hello');
// debouncedSearch('hello w');
// debouncedSearch('hello wo');
// debouncedSearch('hello world');
