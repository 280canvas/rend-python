# Generated from twoeighty.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .twoeightyParser import twoeightyParser
else:
    from twoeightyParser import twoeightyParser

# This class defines a complete generic visitor for a parse tree produced by twoeightyParser.

class twoeightyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by twoeightyParser#program.
    def visitProgram(self, ctx:twoeightyParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by twoeightyParser#variableDec.
    def visitVariableDec(self, ctx:twoeightyParser.VariableDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by twoeightyParser#loop.
    def visitLoop(self, ctx:twoeightyParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by twoeightyParser#statement.
    def visitStatement(self, ctx:twoeightyParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by twoeightyParser#clear.
    def visitClear(self, ctx:twoeightyParser.ClearContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by twoeightyParser#shape.
    def visitShape(self, ctx:twoeightyParser.ShapeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by twoeightyParser#rectangle.
    def visitRectangle(self, ctx:twoeightyParser.RectangleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by twoeightyParser#circle.
    def visitCircle(self, ctx:twoeightyParser.CircleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by twoeightyParser#line.
    def visitLine(self, ctx:twoeightyParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by twoeightyParser#arc.
    def visitArc(self, ctx:twoeightyParser.ArcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by twoeightyParser#increment.
    def visitIncrement(self, ctx:twoeightyParser.IncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by twoeightyParser#decrement.
    def visitDecrement(self, ctx:twoeightyParser.DecrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by twoeightyParser#variableAssign.
    def visitVariableAssign(self, ctx:twoeightyParser.VariableAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by twoeightyParser#Integer.
    def visitInteger(self, ctx:twoeightyParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by twoeightyParser#Variable.
    def visitVariable(self, ctx:twoeightyParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by twoeightyParser#Thousand.
    def visitThousand(self, ctx:twoeightyParser.ThousandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by twoeightyParser#Binop.
    def visitBinop(self, ctx:twoeightyParser.BinopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by twoeightyParser#op.
    def visitOp(self, ctx:twoeightyParser.OpContext):
        return self.visitChildren(ctx)



del twoeightyParser