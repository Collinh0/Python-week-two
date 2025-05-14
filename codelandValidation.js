function codelandUsernameValidation(str) {
    if (str.length < 4 || str.length > 25) {
      return "false";
    }  //Length between 4 and 25 characters
  
    
    if (!/^[a-zA-Z]/.test(str)) {
      return "false";
    }  // Must start with a letter
  
    
    if (!/^[a-zA-Z0-9_]+$/.test(str)) {
      return "false";
    } // Only letters, numbers, and underscores
  
    
    if (str.endsWith("_")) {
      return "false";
    } // Cannot end with an underscore
  
    return "true";
  } 

console.log(codelandUsernameValidation("Asamoah_gian1"))
  console.log(codelandUsernameValidation("1Asamoah_gian"))