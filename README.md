# Face recognition module for Valkyri powered by python

## Description

Valkyri Python Face Module - Version 0.1

## Installation

1. Clone the repo with: `git clone https://gitlab.com/jeyak/valkyri_face_py.git`
2. Run `install_dependency.sh` to install all project dependency
3. Have fun !

## Usage

Option | (or) Long option | Argument | Description 
--- | --- | --- | --- 
-i | --identifie | [path_to_image] | Identifie the face
-a | --add | [user_id] [path_to_image] | Add a face to the face database
-r | --remove | [user_id] | Remove the face of the user id of the database
-u | --update | [user_id] | Update the face of the user id of the database
-di | --display | None | Display all user ids from the database
-m | --user-matrix | [user_id] | Display the matrix of the user
-h | --help | None | Help

## TODO

Option | (or) Long option | Argument | Description 
--- | --- | --- | --- 
n | n | n | n 

 - Test argument error

## Remarque

- sys.stdout.flush() : 
```return the buffer to the node program```

## History

- v0.1.0 (Alpha)

```
- Initial release
```

## Credits



## License

TODO: Write license