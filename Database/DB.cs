using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Data.Common;
using System.Configuration;

namespace DB
{
    // TODO: remove the main method and convert this to a class that we don't run but access as an instance
    // Everything will need to be converted to methods, 
	class DB
    {
        public DB()
        {
            startDB();
        }
        // These methods will not work until we convert the class
        public static void pullAttributes()
        {
            return dataReader["Attributes"];
        }

        public static void pullScans()
        {
            return dataReader["Scans"];
        }

        static void startDB()
        {
            // We are grabbing provider from App.config
            string provider = ConfigurationManager.AppSettings
                ["provider"];

            // Also grabbing connectionString from App.config
            string connectionString =
                ConfigurationManager.AppSettings["connectionString"];
            // Generate an instance of DbProviderFactory
            // So then we use factory to pass queries to our database
            DbProviderFactory factory = 
                DbProviderFactories GetFactory(provider);
            // Create the database connection
            using (DbConnection connection =
                    factory.CreateConnection())
            {
                // Here we verify that we actually have a connection
                if(connection = null)
                {
                    // error catch
                    Console.WriteLine("Connection Error");
                    Console.ReadLine();
                    return;
                }

                // data that is needed to open the correct database
                connection.ConnectionString = connectionString;
                // opens the database connection
                connection.Open();
                //DbCommand allows us to pass queries to the DB
                DbCommand = factory.CreateCommand();
                // catch for a command error
                if(command == null)
                {
                    Console.WriteLine("Command Error");
                    Console.ReadLine();
                    return;
                }

                command.Connection = connection;



                command.CommandText = "INSERT INTO virusInfoTable(name, price) VALUES('Scans','Attributes')";

                // The actual query
                command.CommandText = "Select * From virusInfoTable";      //Assuming the database table is called "virusInfoTable"



                //DbDataReader will read the row results from our query
                using (DbDataReader dataReader =
                    command.ExecuteReader())
                {
                    // cycles through our results
                    while (dataReader.Read())
                    {
                        // Currently just outputs data from rows in scan and attributes
                        Console.WriteLine($"{dataReader["Scans"]} " +
                            $"{dataReader["Attributes"]}")
                    }
                }

                // Keeps console open
                Console.ReadLine();
            }
        }
    }
}