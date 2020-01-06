Sub Homework()
    Dim ws As Worksheet
        For Each ws In ActiveWorkbook.Worksheets
        'Activate the worksheet http://codevba.com/excel/activate_worksheet.htm
        ws.Activate
            'Set last row value
            LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
                'Set the Values to find the ticker, changes and total volume
                Cells(1, 9).Value = "Ticker"
                Cells(1, 10).Value = "Yearly Change"
                Cells(1, 11).Value = "Percent Change"
                Cells(1, 12).Value = "Total Stock Vol"
                'Add variables
                Dim Ticker As String
                Dim Close_Year As Double
                Dim Open_Year As Double
                Dim Yearly_Change As Double
                Dim Percent_Change As Double
                Dim Vol As Double
                Dim Row As Double
                Vol = 0
                Row = 2
                'Open year value
                Open_Year = Cells(2, 3).Value
                'Set up loop to find ticker symbols
                For i = 2 To LastRow
                    If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
                        Ticker = Cells(i, 1).Value
                        Cells(Row, 9).Value = Ticker
                        
                        Close_Year = Cells(i, 6).Value
                        
                        Yearly_Change = Close_Year - Open_Year
                        Cells(Row, 10).Value = Yearly_Change
                        'Nest if to find percent change
                        If (Open_Year = 0 And Close_Year = 0) Then
                            Percent_Change = 0
                        ElseIf (Open_Year = 0 And Close_Year <> 0) Then
                            Percent_Change = 1
                        Else
                            Percent_Change = Yearly_Change / Open_Year
                            Cells(Row, 11).Value = Percent_Change
                            Cells(Row, 11).NumberFormat = "0.00%"
                        End If
                            'Total volume formula
                            Vol = Vol + Cells(i, 7).Value
                            Cells(Row, 12).Value = Vol
                            'Add to the row so we can put in next ticker symbol
                            Row = Row + 1
                            'Reset the Open year price and Volume
                            Open_Year = Cells(i + 1, 3)
                            Vol = 0
                     Else
                            Vol = Vol + Cells(i, 7).Value
                     End If
                Next i
                'Set the year end row
                Year_end_row = ws.Cells(Rows.Count, 9).End(xlUp).Row
                'If statement to set up colors for cells
                For j = 2 To Year_end_row
                    If (Cells(j, 10).Value > 0 Or Cells(j, 10).Value = 0) Then
                        Cells(j, 10).Interior.ColorIndex = 10
                    ElseIf Cells(j, 10).Value < 0 Then
                        Cells(j, 10).Interior.ColorIndex = 3
                    End If
                Next j
                'Set the Values to find the Greatest increase/decrease/total volume
                Cells(2, 15).Value = "Greatest % Increase"
                Cells(3, 15).Value = "Greatest % Decrease"
                Cells(4, 15).Value = "Greatest Total Vol"
                Cells(1, 16).Value = "Ticker"
                Cells(1, 17).Value = "Value"
                'Set if statement to find Max and Min for worksheet (had some help figuring out the formula for the start of this
                'https://stackoverflow.com/questions/31906571/excel-vba-find-maximum-value-in-range-on-specific-sheet
                For k = 2 To Year_end_row
                    If Cells(k, 11).Value = Application.WorksheetFunction.Max(ws.Range("K2:K" & Year_end_row)) Then
                        Cells(2, 16).Value = Cells(k, 9).Value
                        Cells(2, 17).Value = Cells(k, 11).Value
                        Cells(2, 17).NumberFormat = "0.00%"
                    ElseIf Cells(k, 11).Value = Application.WorksheetFunction.Min(ws.Range("K2:K" & Year_end_row)) Then
                        Cells(3, 16).Value = Cells(k, 9).Value
                        Cells(3, 17).Value = Cells(k, 11).Value
                        Cells(3, 17).NumberFormat = "0.00%"
                    ElseIf Cells(k, 12).Value = Application.WorksheetFunction.Max(ws.Range("L2:L" & Year_end_row)) Then
                        Cells(4, 16).Value = Cells(k, 9).Value
                        Cells(4, 17).Value = Cells(k, 12).Value
                   End If
                Next k
            Next ws
        
    End Sub
