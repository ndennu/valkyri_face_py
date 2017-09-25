#!/usr/bin/python3
"""Main module"""
import sys
from face.ValkyriFaceManager import ValkyriFaceManager

def print_help():
    """Display help message"""
    print('Valkyri Python Face Module - Version 0.1\n' +
          'Usage ---\n' +
          '-i \t or \t --identify [path_to_image] \t\t: identify the face\n' +
          '-a \t or \t --add [user_id] [path_to_image] \t: Add a face to the face database\n' +
          '-r \t or \t --remove [user_id] \t\t\t: ' +
          'Remove the face of the user id of the database\n' +
          '-di \t or \t --display \t\t\t\t: Display all user ids from the database\n' +
          '-m \t or \t --user-matrix \t\t\t\t: Display the matrix of user from the database\n' +
          '-h \t or \t --help \t\t\t\t: Help')

def identify(valkyri_face_manager):
    """Identify the face"""
    valkyri_face_manager.deserialize_faces()
    face_matrix = valkyri_face_manager.create_matrix(sys.argv[2])
    if face_matrix is None:
        print(0)
        sys.stdout.flush()
        return 0
    user_id = valkyri_face_manager.find_face(face_matrix)
    print(user_id)
    sys.stdout.flush()
    return user_id

def add_face(valkyri_face_manager):
    """Add a face to the face database"""
    if len(sys.argv) < 4 and isinstance(sys.argv[2], int):
        print(False)
        sys.stdout.flush()
        return False

    valkyri_face_manager.deserialize_faces()

    face_id_count = ValkyriFaceManager.known_faces_id.count(sys.argv[2])

    if sys.argv[2] != 0 and face_id_count == 0:
        face_matrix = valkyri_face_manager.create_matrix(sys.argv[3])
        user_id = valkyri_face_manager.find_face(face_matrix)

        if user_id == 0:
            ValkyriFaceManager.known_faces_id.append(sys.argv[2])
            ValkyriFaceManager.known_faces.append(face_matrix)
            valkyri_face_manager.serialize_faces()
            print(True)
            sys.stdout.flush()
            return True
    return update_face(valkyri_face_manager)

def remove_face(valkyri_face_manager):
    """Remove the face of the user id of the database"""
    if len(sys.argv) < 3:
        print(False)
        sys.stdout.flush()
        return False

    valkyri_face_manager.deserialize_faces()

    try:
        face_index = ValkyriFaceManager.known_faces_id.index(sys.argv[2])

        del ValkyriFaceManager.known_faces[face_index]
        del ValkyriFaceManager.known_faces_id[face_index]

        valkyri_face_manager.serialize_faces()
        print(True)
        sys.stdout.flush()
        return True
    except ValueError:
        print(False)
        sys.stdout.flush()
        return False

def update_face(valkyri_face_manager):
    """Update the face of the user id of the database"""
    if len(sys.argv) < 4:
        print(False)
        sys.stdout.flush()
        return False

    valkyri_face_manager.deserialize_faces()

    try:
        face_index = ValkyriFaceManager.known_faces_id.index(sys.argv[2])

        ValkyriFaceManager.known_faces[face_index] = valkyri_face_manager.create_matrix(sys.argv[3])

        valkyri_face_manager.serialize_faces()
        print(True)
        sys.stdout.flush()
        return True
    except ValueError:
        print(False)
        sys.stdout.flush()
        return False

def display_all(valkyri_face_manager):
    """Display all user ids from the database"""
    valkyri_face_manager.deserialize_faces()
    print(ValkyriFaceManager.known_faces_id)
    sys.stdout.flush()
    return ValkyriFaceManager.known_faces_id

def display_matrix(valkyri_face_manager):
    """Display the matrix of the user"""
    if len(sys.argv) < 3:
        print(False)
        sys.stdout.flush()
        return None
    valkyri_face_manager.deserialize_faces()
    matrix = valkyri_face_manager.get_user_matrix(sys.argv[2])
    print(matrix)
    sys.stdout.flush() # return the buffer to the node program
    return matrix

def main():
    """Main function"""

    if len(sys.argv) < 2:
        print_help()
        return 0
    valkyri_face_manager = ValkyriFaceManager()

    # identify
    # python3 __main__.py -i "path to face image"
    if sys.argv[1] == '-i' or sys.argv[1] == '--identify':
        identify(valkyri_face_manager)
        exit()
    # Add a face
    # python3 __main__.py -a "user id" "path to face image"
    elif sys.argv[1] == '-a' or sys.argv[1] == '--add':
        add_face(valkyri_face_manager)
        exit()
    # Remove a face
    # python3 __main__.py -r "user id"
    elif sys.argv[1] == '-r' or sys.argv[1] == '--remove':
        remove_face(valkyri_face_manager)
        exit()
    # Update a face
    # python3 __main__.py -u "user id"
    elif sys.argv[1] == '-u' or sys.argv[1] == '--update':
        update_face(valkyri_face_manager)
        exit()
    # Display all user ids from the database
    # python3 __main__.py -di "user id"
    elif sys.argv[1] == '-di' or sys.argv[1] == '--display':
        display_all(valkyri_face_manager)
        exit()
    # Display the matrix of the user from the database
    # python3 __main__.py -r "user id"
    elif sys.argv[1] == '-m' or sys.argv[1] == '--user-matrix':
        display_matrix(valkyri_face_manager)
        exit()
    # Help
    # python3 __main__.py -h
    elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print_help()
        exit()
    #if option is uncorrect
    print('Unknown option : ' + sys.argv[1])
    print_help()
    exit()

if __name__ == '__main__':
    main()
