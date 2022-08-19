from Engine.piece import Piece
from Engine.AI.piece_square_tables import Piece_square_table

class Evaluation:

    @classmethod
    def init(cls, board):
        cls.board = board

    @classmethod
    def shef(cls):
        """
        Standard Heuristic Evaluation Function \n
        :return: a heuristic evaluation of current material on board relative to moving color.
        positive: good
        negative: bad
        """
        friendly_eval = cls.static_material_eval(cls.board.moving_side)
        opponent_eval = cls.static_material_eval(cls.board.opponent_side)
        return friendly_eval - opponent_eval

    @classmethod
    def static_material_eval(cls, moving_side):
        mat = 0
        for piece_id in range(1, 7):
            mat += len(cls.board.piece_lists[moving_side][piece_id]) * cls.board.values[piece_id]
        return mat

    @classmethod
    def shef_advanced(cls):
        """
        Advanced Standard Heuristic Evaluation Function \n
        :return: a heuristic piece-square-table-based evaluation of current material on board relative to moving color.
        """
        friendly_eval = cls.pst_material_eval(cls.board.moving_side)
        opponent_eval = cls.pst_material_eval(cls.board.opponent_side)
        return friendly_eval - opponent_eval

    @classmethod  
    def pst_material_eval(cls, moving_side):
        """
        :return: Piece-square-table-based evaluation of moving side's material
        """
        mat = 0
        for piece_id in range(1, 7):
            for square in cls.board.piece_lists[moving_side][piece_id]:
                mat += Piece_square_table.get_pst_value(piece_id, square, moving_side)
        return mat


      

