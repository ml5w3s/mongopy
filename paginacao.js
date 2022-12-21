function printStudents(pageNumber, nPerPage) {
  print( "Page: " + pageNumber );
  db.students.find()
             .sort( { _id: 1 } )
             .skip( pageNumber > 0 ? ( ( pageNumber - 1 ) * nPerPage ) : 0 )
             .limit( nPerPage )
             .forEach( student => {
               print( student.name );
             } );
}
