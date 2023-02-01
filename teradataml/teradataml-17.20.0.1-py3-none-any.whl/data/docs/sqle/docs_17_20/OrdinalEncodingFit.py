def OrdinalEncodingFit(data=None, target_column=None, approach="AUTO", categories=None,
                       ordinal_values=None, start_value=0, default_value=None, **generic_arguments):
    """
        DESCRIPTION:
            OrdinalEncodingFit() function identifies distinct categorical
            values from the input data or a user-defined list and generates
            the distinct categorical values along with the ordinal value for
            each category.


        PARAMETERS:
            data:
                Required Argument.
                Specifies the input data containing the categorical target column.
                Types: teradataml DataFrame

            target_column:
                Required Argument.
                Specifies the name of the categorical input target column.
                Types: str

            approach:
                Optional Argument.
                Specifies whether to determine categories automatically from the
                input data (AUTO approach) or determine categories from the list
                provided by user (LIST approach).
                Default Value: "AUTO"
                Permitted Values: AUTO, LIST
                Types: str

            categories:
                Optional Argument.
                Specifies the list of categories that need to be encoded in the
                desired order.
                Types: str OR list of strs

            ordinal_values:
                Optional Argument.
                Specifies custom ordinal values to replace the categories.
                Types: int OR list of ints

            start_value:
                Optional Argument.
                Specifies the starting value for ordinal values list.
                Default Value: 0
                Types: int

            default_value:
                Optional Argument.
                Specifies the ordinal value to use when category is not found.
                Types: int

            **generic_arguments:
                Specifies the generic keyword arguments SQLE functions accept. Below
                are the generic keyword arguments:
                    persist:
                        Optional Argument.
                        Specifies whether to persist the results of the
                        function in a table or not. When set to True,
                        results are persisted in a table; otherwise,
                        results are garbage collected at the end of the
                        session.
                        Default Value: False
                        Types: bool

                    volatile:
                        Optional Argument.
                        Specifies whether to put the results of the
                        function in a volatile table or not. When set to
                        True, results are stored in a volatile table,
                        otherwise not.
                        Default Value: False
                        Types: bool

                Function allows the user to partition, hash, order or local
                order the input data. These generic arguments are available
                for each argument that accepts teradataml DataFrame as
                input and can be accessed as:
                    * "<input_data_arg_name>_partition_column" accepts str or
                      list of str (Strings)
                    * "<input_data_arg_name>_hash_column" accepts str or list
                      of str (Strings)
                    * "<input_data_arg_name>_order_column" accepts str or list
                      of str (Strings)
                    * "local_order_<input_data_arg_name>" accepts boolean
                Note:
                    These generic arguments are supported by teradataml if
                    the underlying SQL Engine function supports, else an
                    exception is raised.

        RETURNS:
            Instance of OrdinalEncodingFit.
            Output teradataml DataFrames can be accessed using attribute
            references, such as OrdinalEncodingFitObj.<attribute_name>.
            Output teradataml DataFrame attribute names are:
                1. result
                2. output_data


        RAISES:
            TeradataMlException, TypeError, ValueError


        EXAMPLES:
            # Notes:
            #     1. Get the connection to Vantage, before importing the
            #        function in user space.
            #     2. User can import the function, if it is available on
            #        Vantage user is connected to.
            #     3. To check the list of analytic functions available on
            #        Vantage user connected to, use "display_analytic_functions()".

            # Load the example data.
            load_example_data("teradataml", ["titanic"])

            # Create teradataml DataFrame objects.
            titanic = DataFrame.from_table("titanic")

            # Check the list of available analytic functions.
            display_analytic_functions()

            # Import function OrdinalEncodingFit.
            from teradataml import OrdinalEncodingFit

            # Example 1: Identyfying distinct categorical values from the input.
            ordinal_encodingfit_res_1 = OrdinalEncodingFit(target_column='sex',
                                                           data=titanic)

            # Print the result DataFrame.
            print(ordinal_encodingfit_res_1.result)

            # Example 2: Identifying distinct categorical values from the input and
            #            returns the distinct categorical values along with the ordinal
            #            value for each category.
            ordinal_encodingfit_res_2 = OrdinalEncodingFit(target_column='sex',
                                                           approach='LIST',
                                                           categories=['category0', 'category1'],
                                                           ordinal_values=[1, 2],
                                                           start_value=0,
                                                           default_value=-1,
                                                           data=titanic)

            # Print the result DataFrame.
            print(ordinal_encodingfit_res_2.result)

        """