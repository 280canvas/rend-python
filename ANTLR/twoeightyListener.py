# Generated from /home/reece/Programming/rend-python/twoeighty.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .twoeightyParser import twoeightyParser
else:
    from twoeightyParser import twoeightyParser

# This class defines a complete listener for a parse tree produced by twoeightyParser.
class twoeightyListener(ParseTreeListener):

    # Enter a parse tree produced by twoeightyParser#program.
    def enterProgram(self, ctx:twoeightyParser.ProgramContext):
        pass

    # Exit a parse tree produced by twoeightyParser#program.
    def exitProgram(self, ctx:twoeightyParser.ProgramContext):
        pass


    # Enter a parse tree produced by twoeightyParser#variableDec.
    def enterVariableDec(self, ctx:twoeightyParser.VariableDecContext):
        pass

    # Exit a parse tree produced by twoeightyParser#variableDec.
    def exitVariableDec(self, ctx:twoeightyParser.VariableDecContext):
        pass


    # Enter a parse tree produced by twoeightyParser#loop.
    def enterLoop(self, ctx:twoeightyParser.LoopContext):
        pass

    # Exit a parse tree produced by twoeightyParser#loop.
    def exitLoop(self, ctx:twoeightyParser.LoopContext):
        pass


    # Enter a parse tree produced by twoeightyParser#statement.
    def enterStatement(self, ctx:twoeightyParser.StatementContext):
        pass

    # Exit a parse tree produced by twoeightyParser#statement.
    def exitStatement(self, ctx:twoeightyParser.StatementContext):
        pass


    # Enter a parse tree produced by twoeightyParser#clear.
    def enterClear(self, ctx:twoeightyParser.ClearContext):
        pass

    # Exit a parse tree produced by twoeightyParser#clear.
    def exitClear(self, ctx:twoeightyParser.ClearContext):
        pass


    # Enter a parse tree produced by twoeightyParser#colour.
    def enterColour(self, ctx:twoeightyParser.ColourContext):
        pass

    # Exit a parse tree produced by twoeightyParser#colour.
    def exitColour(self, ctx:twoeightyParser.ColourContext):
        pass


    # Enter a parse tree produced by twoeightyParser#shape.
    def enterShape(self, ctx:twoeightyParser.ShapeContext):
        pass

    # Exit a parse tree produced by twoeightyParser#shape.
    def exitShape(self, ctx:twoeightyParser.ShapeContext):
        pass


    # Enter a parse tree produced by twoeightyParser#rectangle.
    def enterRectangle(self, ctx:twoeightyParser.RectangleContext):
        pass

    # Exit a parse tree produced by twoeightyParser#rectangle.
    def exitRectangle(self, ctx:twoeightyParser.RectangleContext):
        pass


    # Enter a parse tree produced by twoeightyParser#circle.
    def enterCircle(self, ctx:twoeightyParser.CircleContext):
        pass

    # Exit a parse tree produced by twoeightyParser#circle.
    def exitCircle(self, ctx:twoeightyParser.CircleContext):
        pass


    # Enter a parse tree produced by twoeightyParser#line.
    def enterLine(self, ctx:twoeightyParser.LineContext):
        pass

    # Exit a parse tree produced by twoeightyParser#line.
    def exitLine(self, ctx:twoeightyParser.LineContext):
        pass


    # Enter a parse tree produced by twoeightyParser#arc.
    def enterArc(self, ctx:twoeightyParser.ArcContext):
        pass

    # Exit a parse tree produced by twoeightyParser#arc.
    def exitArc(self, ctx:twoeightyParser.ArcContext):
        pass


    # Enter a parse tree produced by twoeightyParser#increment.
    def enterIncrement(self, ctx:twoeightyParser.IncrementContext):
        pass

    # Exit a parse tree produced by twoeightyParser#increment.
    def exitIncrement(self, ctx:twoeightyParser.IncrementContext):
        pass


    # Enter a parse tree produced by twoeightyParser#decrement.
    def enterDecrement(self, ctx:twoeightyParser.DecrementContext):
        pass

    # Exit a parse tree produced by twoeightyParser#decrement.
    def exitDecrement(self, ctx:twoeightyParser.DecrementContext):
        pass


    # Enter a parse tree produced by twoeightyParser#variableAssign.
    def enterVariableAssign(self, ctx:twoeightyParser.VariableAssignContext):
        pass

    # Exit a parse tree produced by twoeightyParser#variableAssign.
    def exitVariableAssign(self, ctx:twoeightyParser.VariableAssignContext):
        pass


    # Enter a parse tree produced by twoeightyParser#Integer.
    def enterInteger(self, ctx:twoeightyParser.IntegerContext):
        pass

    # Exit a parse tree produced by twoeightyParser#Integer.
    def exitInteger(self, ctx:twoeightyParser.IntegerContext):
        pass


    # Enter a parse tree produced by twoeightyParser#Variable.
    def enterVariable(self, ctx:twoeightyParser.VariableContext):
        pass

    # Exit a parse tree produced by twoeightyParser#Variable.
    def exitVariable(self, ctx:twoeightyParser.VariableContext):
        pass


    # Enter a parse tree produced by twoeightyParser#Thousand.
    def enterThousand(self, ctx:twoeightyParser.ThousandContext):
        pass

    # Exit a parse tree produced by twoeightyParser#Thousand.
    def exitThousand(self, ctx:twoeightyParser.ThousandContext):
        pass


    # Enter a parse tree produced by twoeightyParser#MathFunc.
    def enterMathFunc(self, ctx:twoeightyParser.MathFuncContext):
        pass

    # Exit a parse tree produced by twoeightyParser#MathFunc.
    def exitMathFunc(self, ctx:twoeightyParser.MathFuncContext):
        pass


    # Enter a parse tree produced by twoeightyParser#Binop.
    def enterBinop(self, ctx:twoeightyParser.BinopContext):
        pass

    # Exit a parse tree produced by twoeightyParser#Binop.
    def exitBinop(self, ctx:twoeightyParser.BinopContext):
        pass


    # Enter a parse tree produced by twoeightyParser#op.
    def enterOp(self, ctx:twoeightyParser.OpContext):
        pass

    # Exit a parse tree produced by twoeightyParser#op.
    def exitOp(self, ctx:twoeightyParser.OpContext):
        pass


    # Enter a parse tree produced by twoeightyParser#funccall.
    def enterFunccall(self, ctx:twoeightyParser.FunccallContext):
        pass

    # Exit a parse tree produced by twoeightyParser#funccall.
    def exitFunccall(self, ctx:twoeightyParser.FunccallContext):
        pass


