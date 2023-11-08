from tictactoe import player, EMPTY, X, O, actions, result, winner


# print(
#     player(
#         [
#             [O, EMPTY, X],
#             [EMPTY, O, O],
#             [X, X, X],
#         ]
#     )
# )

# print(
#     actions(
#         [
#             [O, EMPTY, X],
#             [EMPTY, O, O],
#             [X, EMPTY, X],
#         ]
#     )
# )

# print(
#     result(
#         [
#             [O, EMPTY, X],
#             [EMPTY, O, O],
#             [X, EMPTY, X],
#         ],
#         (2, 1),
#     )
# )

print(
    winner(
        [
            [X, EMPTY, O],
            [O, X, EMPTY],
            [X, O, X],
        ]
    )
)
