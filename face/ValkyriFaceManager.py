"""Valkyri face manager"""
# Dependency :
#
# - face_recognition
# - dlib
# - python_boost
#

import pickle # Module de serialization binaire
import face_recognition


class ValkyriFaceManager:
    """Valkyri face manager class"""

    known_faces = []
    known_faces_id = []

    def __init__(self):
        ValkyriFaceManager.known_faces = []

    @classmethod
    def create_matrix(cls, path):
        """Create matrix will create and return the matrix of the person's face"""
        try:
            image_matrix = face_recognition.load_image_file(path)
            try:
                face_matrix = face_recognition.face_encodings(image_matrix)[0]
                return face_matrix
            except IndexError:
                # If face not detected or not whell positionned
                return None
        except FileNotFoundError:
            return None

    @classmethod
    def find_face(cls, face_matrix):
        """find_face will match and return the id of the person"""
        results = face_recognition.compare_faces(ValkyriFaceManager.known_faces, face_matrix, 0.6)
        try:
            true_index = results.index(True)
            return ValkyriFaceManager.known_faces_id[true_index]
        except ValueError:
            return 0

    @classmethod
    def get_user_matrix(cls, user_id):
        """get_user_matrix will get and return the matrix of the user"""
        try:
            matrix_index = ValkyriFaceManager.known_faces_id.index(user_id)
            return ValkyriFaceManager.known_faces[matrix_index]
        except ValueError:
            return 0

    @classmethod
    def serialize_faces(cls):
        """Serialize known faces, create file if not exist"""
        try:
            with open('KnownFaceDB/known_faces.pickle', 'wb') as picklefile:
                pickle.dump(ValkyriFaceManager.known_faces, picklefile)
            with open('KnownFaceDB/known_faces_id.pickle', 'wb') as picklefile:
                pickle.dump(ValkyriFaceManager.known_faces_id, picklefile)
            return
        except IOError:
            return

    @classmethod
    def deserialize_faces(cls):
        """Deserialize known faces"""
        try:
            with open('KnownFaceDB/known_faces.pickle', 'rb') as picklefile:
                ValkyriFaceManager.known_faces = pickle.load(picklefile)
            with open('KnownFaceDB/known_faces_id.pickle', 'rb') as picklefile:
                ValkyriFaceManager.known_faces_id = pickle.load(picklefile)
            return
        except IOError:
            return
